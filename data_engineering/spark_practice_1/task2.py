"""Module that implement solution of the second task"""
import dataframes as dfs
from pyspark.sql.functions import row_number
from pyspark.sql import SparkSession, DataFrame, Window
from pyspark.sql import functions as f


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    spark = (SparkSession.builder
             .master('local[*]')
             .appName('task2')
             .getOrCreate())
    return spark


def get_top_10_for_each_genre(dataframe: DataFrame) -> DataFrame:
    """Function return top 10 for each genre dataframe"""
    dataframe = dataframe.where(f.col("numVotes") >= 100_000)
    window_spec = Window.partitionBy("genre").orderBy(f.desc("averageRating"))
    dataframe = dataframe.select("tconst", "primaryTitle",
                                 "numVotes", "averageRating",
                                 "startYear", f.explode("genres").alias("genre"))
    dataframe = dataframe.withColumn("row_n",
                                     row_number().over(window_spec)).where(f.col("row_n") <= 10)
    return dataframe


def get_films_with_ratings(spark) -> DataFrame:
    """Function join films and ratings dataframes and return the result"""
    df1 = dfs.get_title_basics_df(spark, "./data/title.basics.tsv")
    df2 = (dfs.get_title_ratings_df(spark, "./data/title.ratings.tsv")
           .withColumnRenamed("tconst", "r_tconst"))
    dataframe = df1.join(df2, df1.tconst == df2.r_tconst)
    return dataframe


def save_df_to_csv(dataframe: DataFrame, path: str):
    """Function save dataframe to csv file"""
    dataframe.write.option("delimiter", "\t").csv(path)


def main():
    """Main function"""
    spark = get_spark_session()
    dataframe = get_films_with_ratings(spark)
    columns = ["tconst", "primaryTitle", "numVotes", "genre", "averageRating", "startYear"]
    save_df_to_csv(get_top_10_for_each_genre(dataframe).select(columns),
                   "./output/top_for_each_genre.tcv")


if __name__ == '__main__':
    main()
