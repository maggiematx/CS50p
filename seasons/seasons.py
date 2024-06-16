from datetime import datetime, date
import inflect
import sys

class Age:
    def __init__(self, days):
        self.days = days

    def display_minutes(self):
        total_minutes = self.days * 24 * 60  # Convert days to minutes
        return total_minutes

def main():
    birth_date = get_birthday()
    age_in_days = calculate_age_in_days(birth_date)
    age = Age(age_in_days)

    total_minutes = age.display_minutes()
    total_minutes_in_words = convert_minutes_to_words(total_minutes)

    print(total_minutes_in_words)

def get_birthday():
    while True:
        birthday_str = input("Date of Birth (YYYY-MM-DD): ")
        try:
            birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()
            return birthday
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            continue

def calculate_age_in_days(birth_date):
    today = date.today()
    age_in_days = (today - birth_date).days
    return age_in_days

def convert_minutes_to_words(total_minutes):
    p = inflect.engine()
    total_minutes_in_words = p.number_to_words(total_minutes)
    total_minutes_in_words = total_minutes_in_words.replace(" and", "")

    # Insert comma after "thousand" if present
    if "thousand" in total_minutes_in_words:
        total_minutes_in_words = total_minutes_in_words.replace("thousand ", "thousand, ", 1)

    # Capitalize the first letter and add " minutes" at the end
    total_minutes_in_words = total_minutes_in_words.capitalize() + " minutes"
    return total_minutes_in_words

if __name__ == "__main__":
    main()




