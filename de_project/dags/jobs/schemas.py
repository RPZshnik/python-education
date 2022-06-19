"""Module with pyspark dataframe's schemas"""
from pyspark.sql import types

tmdb_schema = types.StructType(fields=[
    types.StructField("adult", types.BooleanType()),
    types.StructField("backdrop_path", types.StringType()),
    types.StructField("belongs_to_collection", types.StringType()),
    types.StructField("budget", types.LongType()),
    types.StructField("genres",
                      types.ArrayType
                      (types.StructType(fields=[types.StructField("id",
                                                                  types.LongType()),
                                                types.StructField("name",
                                                                  types.StringType())]))),
    types.StructField("homepage", types.StringType()),
    types.StructField("id", types.LongType()),
    types.StructField("imdb_id", types.StringType()),
    types.StructField("original_language", types.StringType()),
    types.StructField("original_title", types.StringType()),
    types.StructField("overview", types.StringType()),
    types.StructField("popularity", types.DoubleType()),
    types.StructField("poster_path", types.StringType()),
    types.StructField("production_companies", types.StringType()),
    types.StructField("production_countries", types.StringType()),
    types.StructField("release_date", types.StringType()),
    types.StructField("revenue", types.IntegerType()),
    types.StructField("runtime", types.IntegerType()),
    types.StructField("spoken_languages", types.StringType()),
    types.StructField("status", types.StringType()),
    types.StructField("tagline", types.StringType()),
    types.StructField("title", types.StringType()),
    types.StructField("video", types.BooleanType()),
    types.StructField("vote_average", types.DoubleType()),
    types.StructField("vote_count", types.IntegerType())
])
