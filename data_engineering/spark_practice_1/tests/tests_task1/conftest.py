import pytest
from pyspark import Row
from pyspark.sql import SparkSession


@pytest.fixture(scope='session', autouse=True)
def spark_session():
    """Fixture that enables SparkSession during tests run.

    Yields:
        SparkSession: current SparkSession
    """

    spark_session = SparkSession.builder.getOrCreate()
    spark_session.conf.set("spark.sql.session.timeZone", "UTC")

    yield spark_session

    spark_session.sparkContext.stop()


@pytest.fixture()
def title_basics(spark_session):
    """Fixture of title_basic.

    Yields:
        DataFrame: title_basic dataframe fixture
    """
    spark_session = SparkSession.builder.getOrCreate()

    test_titles_df = spark_session.createDataFrame([
        Row(tconst='tt0000001', titleType='short',
            primaryTitle='Carmencita', originalTitle='Carmencita',
            isAdult="0", startYear="1894", endYear=r"\N", runtimeMinutes="1",
            genres="Documentary,Short"),
        Row(tconst='tt0000002', titleType='short',
            primaryTitle='Le clown et ses chiens', originalTitle='Le clown et ses chiens',
            isAdult="0", startYear="1892", endYear=r"\N", runtimeMinutes="5",
            genres="Animation,Short"),
        Row(tconst='tt0000003', titleType='short',
            primaryTitle='Pauvre Pierrot', originalTitle='Pauvre Pierrot',
            isAdult="0", startYear="2020", endYear=r"\N", runtimeMinutes="4",
            genres="Animation,Comedy,Romance"),
        Row(tconst='tt0000004', titleType='short',
            primaryTitle='Un bon bock', originalTitle='Un bon bock',
            isAdult="0", startYear="1892", endYear=r"\N", runtimeMinutes="12",
            genres="Animation,Short"),
    ])
    return test_titles_df


@pytest.fixture()
def title_ratings(spark_session):
    """Fixture of title_ratings.

    Yields:
        DataFrame: title_basic dataframe fixture
    """
    spark_session = SparkSession.builder.getOrCreate()

    test_ratings_df = spark_session.createDataFrame([
        Row(tconst='tt0000001', averageRating='5.7', numVotes='188200'),
        Row(tconst='tt0000002', averageRating='5.9', numVotes='250'),
        Row(tconst='tt0000003', averageRating='6.5', numVotes='166400'),
        Row(tconst='tt0000004', averageRating='5.8', numVotes='163000')
    ])
    return test_ratings_df


@pytest.fixture()
def title_basics_ratings(spark_session):
    """Fixture of title_ratings.

    Yields:
        DataFrame: title_basic dataframe fixture
    """
    spark_session = SparkSession.builder.getOrCreate()

    test_df = spark_session.createDataFrame([
        Row(tconst='tt0000001', titleType='movie',
            primaryTitle='Carmencita', originalTitle='Carmencita',
            isAdult="0", startYear="1894", endYear=r"\N", runtimeMinutes="1",
            genres="Documentary,Short", r_tconst='tt0000001', averageRating='5.7', numVotes='188200'),
        Row(tconst='tt0000002', titleType='short',
            primaryTitle='Le clown et ses chiens', originalTitle='Le clown et ses chiens',
            isAdult="0", startYear="1892", endYear=r"\N", runtimeMinutes="5",
            genres="Animation,Short", r_tconst='tt0000002', averageRating='5.9', numVotes='250'),
        Row(tconst='tt0000003', titleType='movie',
            primaryTitle='Pauvre Pierrot', originalTitle='Pauvre Pierrot',
            isAdult="0", startYear="2020", endYear=r"\N", runtimeMinutes="4",
            genres="Animation,Comedy,Romance", r_tconst='tt0000003', averageRating='6.5', numVotes='166400'),
        Row(tconst='tt0000004', titleType='movie',
            primaryTitle='Un bon bock', originalTitle='Un bon bock',
            isAdult="0", startYear="1892", endYear=r"\N", runtimeMinutes="12",
            genres="Animation,Short", r_tconst='tt0000004', averageRating='5.8', numVotes='163000'),
    ])
    return test_df
