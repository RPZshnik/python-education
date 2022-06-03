from data_engineering.spark_practice_1.tests.tests_task1.utils import dfs_equal
from pyspark.sql.types import Row
from data_engineering.spark_practice_1.task1 import get_top_all_the_time


def test_get_top_all_the_time(spark_session):
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
    expected_df = spark_session.createDataFrame([
        Row(tconst='tt0000003', titleType='movie',
            primaryTitle='Pauvre Pierrot', originalTitle='Pauvre Pierrot',
            isAdult="0", startYear="2020", endYear=r"\N", runtimeMinutes="4",
            genres="Animation,Comedy,Romance", r_tconst='tt0000003', averageRating='6.5', numVotes='166400'),
        Row(tconst='tt0000004', titleType='movie',
            primaryTitle='Un bon bock', originalTitle='Un bon bock',
            isAdult="0", startYear="1892", endYear=r"\N", runtimeMinutes="12",
            genres="Animation,Short", r_tconst='tt0000004', averageRating='5.8', numVotes='163000'),
        Row(tconst='tt0000001', titleType='movie',
            primaryTitle='Carmencita', originalTitle='Carmencita',
            isAdult="0", startYear="1894", endYear=r"\N", runtimeMinutes="1",
            genres="Documentary,Short", r_tconst='tt0000001', averageRating='5.7', numVotes='188200')
    ])
    result_df = get_top_all_the_time(test_df)
    assert dfs_equal(result_df, expected_df)
