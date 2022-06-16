from data_engineering.spark_practice_1.tests.tests_task1.utils import dfs_equal
from pyspark.sql.types import Row
from data_engineering.spark_practice_1.task1 import get_top_between


def test_get_top_between(spark_session, title_basics_ratings):
    test_df = title_basics_ratings
    test_df.show()
    expected_df = spark_session.createDataFrame([
        Row(tconst='tt0000001', titleType='movie',
            primaryTitle='Carmencita', originalTitle='Carmencita',
            isAdult="0", startYear="1894", endYear=r"\N", runtimeMinutes="1",
            genres="Documentary,Short", r_tconst='tt0000001', averageRating='5.7', numVotes='188200')
    ])
    result_df = get_top_between(test_df, 1893, 2000)
    result_df.show()
    assert dfs_equal(result_df, expected_df)
