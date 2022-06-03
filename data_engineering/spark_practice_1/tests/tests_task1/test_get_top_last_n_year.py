from data_engineering.spark_practice_1.tests.tests_task1.utils import dfs_equal
from pyspark.sql.types import Row
from data_engineering.spark_practice_1.task1 import get_top_last_n_years


def test_get_top_last_n_year(spark_session, test_title_basics_ratings):
    test_df = test_title_basics_ratings
    expected_df = spark_session.createDataFrame([
        Row(tconst='tt0000003', titleType='movie',
            primaryTitle='Pauvre Pierrot', originalTitle='Pauvre Pierrot',
            isAdult="0", startYear="2020", endYear=r"\N", runtimeMinutes="4",
            genres="Animation,Comedy,Romance", r_tconst='tt0000003', averageRating='6.5', numVotes='166400'),
    ])
    result_df = get_top_last_n_years(test_df, 10)
    assert dfs_equal(result_df, expected_df)
