import pytest
from datetime import datetime, date, timedelta
from seasons import Age, get_birthday, calculate_age_in_timedelta, convert_minutes_to_words  # Replace with your actual module name
import inflect

# Mock input to simulate user input for get_birthday function
def mock_input(prompt):
    inputs = {
        "Date of Birth: ": "2023-06-15"
    }
    return inputs[prompt]

def test_get_birthday(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2023-06-15")
    birthday = get_birthday()
    assert birthday == date(2023, 6, 15)

    monkeypatch.setattr('builtins.input', lambda _: "2022-06-15")
    birthday = get_birthday()
    assert birthday == date(2022, 6, 15)

    monkeypatch.setattr('builtins.input', lambda _: "invalid_date")
    with pytest.raises(SystemExit):  # This tests for sys.exit(1) on invalid date
        get_birthday()

def test_calculate_age_in_timedelta():
    birth_date = date(2023, 6, 15)
    today_date = date(2024, 6, 15)
    age_in_timedelta = calculate_age_in_timedelta(birth_date)
    assert age_in_timedelta.days == (today_date - birth_date + timedelta(days=1)).days

    birth_date = date(2022, 6, 15)
    today_date = date(2024, 6, 15)
    age_in_timedelta = calculate_age_in_timedelta(birth_date)
    assert age_in_timedelta.days == (today_date - birth_date + timedelta(days=1)).days

def test_display_minutes():
    age_in_timedelta = timedelta(days=365)
    age = Age(age_in_timedelta)
    assert age.display_minutes() == 525600

    age_in_timedelta = timedelta(days=730)
    age = Age(age_in_timedelta)
    assert age.display_minutes() == 1051200

def test_convert_minutes_to_words():
    p = inflect.engine()

    total_minutes = 2861280
    expected_output = p.number_to_words(total_minutes).replace(" and", "")
    if "thousand" in expected_output:
        expected_output = expected_output.replace("thousand ", "thousand, ", 1)
    expected_output = expected_output.capitalize()

    assert convert_minutes_to_words(total_minutes) == expected_output

if __name__ == "__main__":
    pytest.main()
