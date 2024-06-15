from datetime import datetime, date
import inflect
import sys

class Age:
    def __init__(self, timedelta):
        self.timedelta = timedelta

    def display_minutes(self):
        total_minutes = self.timedelta.total_seconds() / 60
        return int(total_minutes)

def main():
    birth_date = get_birthday()
    age_in_timedelta = calculate_age_in_timedelta(birth_date)
    age = Age(age_in_timedelta)

    total_minutes = age.display_minutes()
    total_minutes_in_words = convert_minutes_to_words(total_minutes)

    print(f"{total_minutes_in_words} minutes")

def get_birthday():
    while True:
        birthday_str = input("Date of Birth (YYYY-MM-DD): ")
        try:
            birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()
            return birthday
        except ValueError:
            print("Invalid date. Please use the format YYYY-MM-DD.")
            sys.exit(1)

def calculate_age_in_timedelta(birth_date):
    today = datetime.now().date()
    age_in_timedelta = today - birth_date
    return age_in_timedelta

def convert_minutes_to_words(total_minutes):
    p = inflect.engine()
    total_minutes_in_words = p.number_to_words(total_minutes)
    total_minutes_in_words = total_minutes_in_words.replace(",", "").replace(" and", "")
    return total_minutes_in_words

if __name__ == "__main__":
    main()

