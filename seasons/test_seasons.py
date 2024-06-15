from seasons import get_birthday, calculate_age_in_timedelta,convert_minutes_to_words
import pytest

def test_get_birthday():
    assert get_birthday("2023-6-15") == Five hundred twenty-seven thousand, forty minutes
    assert get_birthday("2022-06-15") == 
    assert convert("6/6") == 100


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1)=="E"
    assert gauge(99)=="F"


def test_value_error():
    with pytest.raises(ValueError):
        convert("x/y")

def test_zero_divison_error():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
