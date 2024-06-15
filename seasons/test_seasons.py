from datetime import datetime
from seasons import get_birthday, calculate_age_in_timedelta, convert_minutes_to_words
import pytest

def test_get_birthday():
    assert get_birthday() == "Five hundred twenty-seven thousand, forty minutes"
    assert get_birthday() == "One million, fifty-two thousand, six hundred forty minutes"
    assert get_birthday() == "Invalid date"


def test_convert_minutes_to_words():
    assert convert_minutes_to_words(2861280) == "Two million, eight hundred sixty-one thousand, two hundred eighty minutes"

if __name__ == "__main__":
    pytest.main()

