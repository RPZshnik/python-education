"""Module that implement solution of the fourth task"""
import dataframes as dfs
from pyspark import SparkConf
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as f


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    config = SparkConf().setAll([('spark.executor.memory', '8g')])
    spark = SparkSession.builder\
        .config(conf=config)\
        .master('local')\
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


def get_top_all_time(spark) -> DataFrame:
    """Function return top films during all th time"""
    dataframe = get_films_with_ratings(spark)
    dataframe = dataframe.where(dataframe["numVotes"] >= 10**5)\
        .orderBy(dataframe["averageRating"], ascending=False)
    return dataframe


def get_demanded_actors(dataframe: DataFrame) -> DataFrame:
    """Function return dataframe with demanded actors"""
    dataframe = dataframe.groupBy("primaryName").count()\
        .orderBy(f.col("count"), ascending=False).select("primaryName")
    return dataframe


def save_df_to_csv(dataframe: DataFrame, path: str):
    """Function save dataframe to csv file"""
    dataframe.write.option("delimiter", "\t").csv(path)


def main():
    """Main function"""
    spark = get_spark_session()

    dataframe = get_top_all_time(spark).limit(10000)
    names_dataframe = dfs.get_name_basics_df(spark, "./data/name.basics.tsv")
    principals_df = dfs.get_title_principals_df(spark, "./data/title.principals.tsv") \
        .where(f.col("category") == "actor")
    dataframe = principals_df.join(dataframe, dataframe.tconst == principals_df.tconst) \
        .join(names_dataframe, principals_df.nconst == names_dataframe.nconst)

    save_df_to_csv(get_demanded_actors(dataframe), "./output/demanded_actors.csv")


if __name__ == '__main__':
    main()
