from datetime import datetime
import inflect
import sys

class Age:
    def __init__(self, timedelta):
        self.timedelta = timedelta

    def display_minutes(self):
        total_minutes = self.timedelta.total_seconds() // 60
        return total_minutes

def main():
    birth_date = get_birthday()
    age_in_timedelta = calculate_age_in_timedelta(birth_date)
    age = Age(age_in_timedelta)

    total_minutes = age.display_minutes()
    total_minutes_in_words = convert_minutes_to_words(total_minutes)

    print(f"{total_minutes_in_words} minutes")

def get_birthday():
    while True:
        birthday_str = input("




