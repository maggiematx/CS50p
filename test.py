from datetime import datetime, timedelta
import inflect

class Age:
    def __init__(self, timedelta):
        self.timedelta = timedelta

    def display_minutes(self):
        # Calculate the total number of minutes
        total_seconds = self.timedelta.total_seconds()
        total_minutes = total_seconds // 60  # Convert seconds to minutes
        return int(total_minutes)

def main():
    birth_date = datetime.strptime("2023-04-16", "%Y-%m-%d").date()
    age_in_timedelta = calculate_age_in_timedelta(birth_date)
    age = Age(age_in_timedelta)

    total_minutes = age.display_minutes()
    total_minutes_in_words = convert_minutes_to_words(total_minutes)

    print(f"{total_minutes_in_words} minutes")

def calculate_age_in_timedelta(birth_date):
    today = datetime.now().date()  # Get today's date
    # Calculate the timedelta between today and the birth_date
    age_in_timedelta = today - birth_date
    return age_in_timedelta

def convert_minutes_to_words(total_minutes):
    p = inflect.engine()
    total_minutes_in_words = p.number_to_words(total_minutes)
    # Replace commas and "and"
    total_minutes_in_words = total_minutes_in_words.replace(",", "").replace(" and", "")
    return total_minutes_in_words

if __name__ == "__main__":
    main()
