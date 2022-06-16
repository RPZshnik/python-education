"""Module that implement solution of the fifth task"""
import dataframes as dfs
from pyspark import SparkConf
from pyspark.sql.functions import row_number
from pyspark.sql import SparkSession, DataFrame, Window
from pyspark.sql import functions as f


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    config = SparkConf().setAll([('spark.executor.memory', '16g')])
    spark = (SparkSession.builder
             .config(conf=config)
             .master('local[*]')
             .appName('task5')
             .getOrCreate())
    return spark


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

    titles_df = get_films_with_ratings(spark)
    crew_df = dfs.get_title_crew_df(spark, "./data/title.crew.tsv")
    names_df = dfs.get_name_basics_df(spark, "./data/name.basics.tsv")
    directors = crew_df.select("tconst", f.explode("directors").alias("director"))

    dataframe = (titles_df.join(directors, titles_df.tconst == directors.tconst)
                 .select("director", "primaryTitle", "startYear", "averageRating", "numVotes"))
    dataframe = dataframe.join(names_df, dataframe.director == names_df.nconst)

    window_spec_1 = Window.partitionBy("director").orderBy(f.desc("averageRating"))
    dataframe = dataframe.withColumn("row",
                                     row_number().over(window_spec_1)).where(f.col("row") <= 5)

    dataframe = dataframe.select("primaryName", "primaryTitle",
                                 "startYear", "averageRating", "numVotes")

    save_df_to_csv(dataframe, "./output/task5.csv")


if __name__ == '__main__':
    main()
