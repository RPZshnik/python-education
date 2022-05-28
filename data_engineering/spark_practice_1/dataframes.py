from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, BooleanType, DataType, DateType, IntegerType, ArrayType, FloatType
from pyspark.sql import functions as f


def get_df_from_tsv(spark: SparkSession, path: str, schema=None):
    df = spark.read.csv(path, sep=r'\t',
                        header=True,
                        schema=schema)
    return df


def get_title_basics_df(spark: SparkSession, path: str):
    schema = StructType() \
        .add("tconst", StringType(), True) \
        .add("titleType", StringType(), True) \
        .add("primaryTitle", StringType(), True) \
        .add("originalTitle", StringType(), True) \
        .add("isAdult", BooleanType(), True) \
        .add("startYear", IntegerType(), True) \
        .add("endYear", IntegerType(), True) \
        .add("runtimeMinutes", IntegerType(), True) \
        .add("genres", StringType(), True)
    df = get_df_from_tsv(spark, path, schema)
    df = df.withColumn("genres", f.split(f.col("genres"), ","))
    return df


def get_title_akas_df(spark: SparkSession, path: str):
    schema = StructType() \
        .add("titleId", StringType(), True) \
        .add("ordering", IntegerType(), True) \
        .add("title", StringType(), True) \
        .add("region", StringType(), True) \
        .add("language", StringType(), True) \
        .add("types", StringType(), True) \
        .add("attributes", StringType(), True) \
        .add("isOriginalTitle", BooleanType(), True)
    df = get_df_from_tsv(spark, path, schema)
    df = df.withColumn("types", f.split(f.col("types"), ","))
    df = df.withColumn("attributes", f.split(f.col("attributes"), ","))
    return df


def get_title_crew_df(spark: SparkSession, path: str):
    schema = StructType() \
        .add("tconst", StringType(), True) \
        .add("directors", StringType(), True) \
        .add("writers", StringType(), True)
    df = get_df_from_tsv(spark, path, schema)
    df = df.withColumn("directors", f.split(f.col("directors"), ","))
    df = df.withColumn("writers", f.split(f.col("writers"), ","))
    return df


def get_title_episode_df(spark: SparkSession, path: str):
    schema = StructType() \
        .add("tconst", StringType(), True) \
        .add("parentTconst", StringType(), True) \
        .add("seasonNumber", IntegerType(), True) \
        .add("episodeNumber", IntegerType(), True)
    df = get_df_from_tsv(spark, path, schema)
    return df


def get_title_principals_df(spark: SparkSession, path: str):
    schema = StructType() \
        .add("tconst", StringType(), True) \
        .add("ordering", IntegerType(), True) \
        .add("nconst", StringType(), True) \
        .add("category", StringType(), True) \
        .add("job", StringType(), True) \
        .add("characters", StringType(), True)
    df = get_df_from_tsv(spark, path, schema)
    return df


def get_title_ratings_df(spark: SparkSession, path: str):
    schema = StructType() \
        .add("tconst", StringType(), True) \
        .add("averageRating", FloatType(), True) \
        .add("numVotes", IntegerType(), True)
    df = get_df_from_tsv(spark, path, schema)

    return df


def get_name_basics_df(spark: SparkSession, path: str):
    schema = StructType() \
        .add("nconst", StringType(), True) \
        .add("primaryName", StringType(), True) \
        .add("birthYear", DataType(), True) \
        .add("deathYear", DateType(), True) \
        .add("primaryProfession", StringType(), True) \
        .add("knownForTitles", StringType, True)
    df = get_df_from_tsv(spark, path, schema)
    df = df.withColumn("primaryProfession", f.split(f.col("primaryProfession"), ","))
    df = df.withColumn("knownForTitles", f.split(f.col("knownForTitles"), ","))
    return df
