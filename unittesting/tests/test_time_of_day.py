import datetime
from freezegun import freeze_time
from unittesting.to_test import time_of_day


@freeze_time("2022-04-26 04:47:18")
def test_to_night():
    """Test with nighttime"""
    assert time_of_day() == "night"


@freeze_time("2022-04-26 08:13:08")
def test_to_morning():
    """Test with morning-time"""
    assert time_of_day() == "morning"


@freeze_time("2022-04-26 17:30:00")
def test_to_afternoon():
    """Test with afternoon-time"""
    assert time_of_day() == "afternoon"


def test_mock_time_of_day(monkeypatch):
    """Test using monkeypatch"""
    fake_time = datetime.datetime(2022, 2, 26, 12, 0, 0)

    def mock_datetime(*args, **kwargs):
        return fake_time

    monkeypatch.setattr(datetime, "datetime", mock_datetime)
    assert time_of_day() == "afternoon"
