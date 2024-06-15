from datetime import datetime
from seasons import get_birthday, calculate_age_in_timedelta, convert_minutes_to_words
import pytest

def test_get_birthday():
    assert get_birthday("2023-06-15") == "Five hundred twenty-seven thousand, forty minutes"
    assert get_birthday("2022-06-15") == "One million fifty-two thousand, six hundred forty minutes"
    assert get_birthday("January 1, 1987") == None  # Assuming get_birthday returns None on invalid date

def test_calculate_age_in_timedelta():
    birth_date = datetime(2000, 1, 1).date()
    expected_age = calculate_age_in_timedelta(birth_date)
    assert expected_age.days == 2861280  # Adjust based on your calculation logic

def test_convert_minutes_to_words():
    assert convert_minutes_to_words(2861280) == "Two million, eight hundred sixty-one thousand, two hundred eighty minutes"

if __name__ == "__main__":
    pytest.main()

