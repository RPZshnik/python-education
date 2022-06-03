from data_engineering.spark_practice_1.tests.tests_task1.utils import dfs_equal
from unittest.mock import patch
from pyspark.sql.types import Row
from data_engineering.spark_practice_1.task1 import get_films_with_ratings


@patch('task1.dfs.get_title_ratings_df')
@patch('task1.dfs.get_title_basics_df')
def test_get_films_with_ratings(titles_mock, rating_mock, spark_session,
                                test_title_basics, test_title_ratings):
    test_titles_df = test_title_basics
    test_ratings_df = test_title_ratings
    expected_df = spark_session.createDataFrame([
        Row(tconst='tt0000001', titleType='short',
            primaryTitle='Carmencita', originalTitle='Carmencita',
            isAdult="0", startYear="1894", endYear=r"\N", runtimeMinutes="1",
            genres="Documentary,Short", r_tconst='tt0000001', averageRating='5.7', numVotes='188200'),
        Row(tconst='tt0000002', titleType='short',
            primaryTitle='Le clown et ses chiens', originalTitle='Le clown et ses chiens',
            isAdult="0", startYear="1892", endYear=r"\N", runtimeMinutes="5",
            genres="Animation,Short", r_tconst='tt0000002', averageRating='5.9', numVotes='250'),
        Row(tconst='tt0000003', titleType='short',
            primaryTitle='Pauvre Pierrot', originalTitle='Pauvre Pierrot',
            isAdult="0", startYear="2020", endYear=r"\N", runtimeMinutes="4",
            genres="Animation,Comedy,Romance", r_tconst='tt0000003', averageRating='6.5', numVotes='166400'),
        Row(tconst='tt0000004', titleType='short',
            primaryTitle='Un bon bock', originalTitle='Un bon bock',
            isAdult="0", startYear="1892", endYear=r"\N", runtimeMinutes="12",
            genres="Animation,Short", r_tconst='tt0000004', averageRating='5.8', numVotes='163000'),
    ])
    titles_mock.return_value = test_titles_df
    rating_mock.return_value = test_ratings_df
    result_df = get_films_with_ratings(spark_session)
    assert dfs_equal(result_df, expected_df)
