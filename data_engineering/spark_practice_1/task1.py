"""Module that implement solution of the first task"""
import datetime
import dataframes as dfs
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as f


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    spark = SparkSession.builder\
        .master('local[*]')\
        .appName('task1')\
        .getOrCreate()
    return spark


def get_films_with_ratings(spark) -> DataFrame:
    """Function join films and ratings dataframes and return the result"""
    df1 = dfs.get_title_basics_df(spark, "./data/title.basics.tsv")
    df2 = dfs.get_title_ratings_df(spark, "./data/title.ratings.tsv")\
        .withColumnRenamed("tconst", "r_tconst")
    dataframe = df1.join(df2, df1.tconst == df2.r_tconst)
    return dataframe


def get_top_all_the_time(spark) -> DataFrame:
    """Function return top films during all th time"""
    dataframe = get_films_with_ratings(spark)
    dataframe = dataframe.where(f.col("numVotes") >= 10**5)\
        .where(f.col("titleType") == "movie")\
        .orderBy(dataframe["averageRating"], ascending=False)
    return dataframe


def get_top_last_n_years(spark, years: int) -> DataFrame:
    """Function return top films over the past n years"""
    current_year = datetime.datetime.now().year
    dataframe = get_top_all_the_time(spark)\
        .where(f.col("startYear") >= (current_year - years))
    return dataframe


def get_top_between(spark, start_year: int, end_year: int) -> DataFrame:
    """Function return top films between two years"""
    dataframe = get_top_all_the_time(spark)
    dataframe = dataframe\
        .filter((f.col("startYear") >= start_year) &
                (f.col("startYear") <= end_year))
    return dataframe


def save_df_to_csv(dataframe: DataFrame, path: str):
    dataframe.write.option("delimiter", "\t").csv(path)


def main():
    """Main function"""
    spark = get_spark_session()
    columns = ["tconst", "primaryTitle", "numVotes", "averageRating", "startYear"]
    save_df_to_csv(get_top_all_the_time(spark).select(columns), "./output/top_all_time.tsv")
    save_df_to_csv(get_top_last_n_years(spark, 10).select(columns), "./output/top_last_n_year.tsv")
    save_df_to_csv(get_top_between(spark, 1960, 1969).select(columns), "./output/top_sixties.tsv")


if __name__ == '__main__':
    main()
