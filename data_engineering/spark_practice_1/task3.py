"""Module that implement solution of the third task"""
from functools import reduce
from pyspark.sql import SparkSession, DataFrame, Window
from pyspark.sql.functions import row_number
from pyspark.sql import functions as f
import dataframes as dfs


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    spark = SparkSession.builder \
        .master('local[*]') \
        .appName('task1') \
        .getOrCreate()
    return spark


def get_films_with_ratings(spark: SparkSession) -> DataFrame:
    """Function join films and ratings dataframes and return the result"""
    df1 = dfs.get_title_basics_df(spark, "./data/title.basics.tsv")
    df2 = dfs.get_title_ratings_df(spark, "./data/title.ratings.tsv")\
        .withColumnRenamed("tconst", "r_tconst")
    dataframe = df1.join(df2, df1.tconst == df2.r_tconst)
    return dataframe


def get_top_between(dataframe: DataFrame, start_year: int, end_year: int) -> DataFrame:
    """Function return top films between two years"""
    dataframe = dataframe \
        .filter((f.col("startYear") >= start_year) &
                (f.col("startYear") <= end_year))
    return dataframe


def get_top_10_for_each_genre(dataframe: DataFrame) -> DataFrame:
    """Function return top 10 for each genre dataframe"""
    dataframe = dataframe.where(f.col("numVotes") >= 10 ** 5)
    window_spec = Window.partitionBy("genre").orderBy(f.desc("averageRating"))
    dataframe = dataframe.select("tconst", "primaryTitle",
                                 "numVotes", "averageRating",
                                 "startYear", f.explode("genres").alias("genre"))
    dataframe = dataframe.withColumn("row_n",
                                     row_number().over(window_spec)).where(f.col("row_n") <= 10)
    return dataframe


def get_top_each_genre_in_decade(dataframe: DataFrame) -> DataFrame:
    """Function return top 10 for each genre in every decade dataframe"""
    def get_by_decade():
        for year in range(2020, 1949, -10):
            yield get_top_between(dataframe, year, year + 10)

    def union(prev_element: DataFrame, element: DataFrame):
        return prev_element.union(element)

    dataframe = reduce(union, [get_top_10_for_each_genre(df) for df in get_by_decade()])
    dataframe = dataframe.withColumn("yearRange",
                                     f.concat_ws("-", f.floor(f.col('startYear') / 10) * 10,
                                                 f.floor(f.col('startYear') / 10 + 1) * 10))
    return dataframe


def save_df_to_csv(dataframe: DataFrame, path: str):
    """Function save dataframe to csv file"""
    dataframe.write.option("delimiter", "\t").csv(path)


def main():
    """Main function"""
    spark = get_spark_session()
    dataframe = get_films_with_ratings(spark)
    columns = ["tconst", "primaryTitle", "startYear", "genre", "averageRating", "yearRange"]
    save_df_to_csv(get_top_each_genre_in_decade(dataframe)
                   .select(columns), "./output/task3.csv")


if __name__ == '__main__':
    main()
