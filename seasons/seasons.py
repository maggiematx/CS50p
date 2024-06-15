from datetime import datetime, date, timedelta
import inflect

class Age:
    def __init__(self,timedelta):
        self.timedelta=timedelta


    def display_minutes(self):
        total_seconds = self.timedelta.total_seconds()
        total_minutes = total_seconds // 60  # Convert seconds to minutes
        return int(total_minutes)

def main():
    birth_date=datetime.strptime("%Y-%m-%d").date()
    age_in_timedelta=calculate_age_in_timedelta(birth_date)
    age=Age(age_in_timedelta)

    total_minutes=age.display_minutes()
    total_minutes_in_words=convert_minutes_to_words(total_minutes)

    print(total_minutes_in_words, "minutes")


def get_birthday():
    while True:
        birthday_str=input("Date of Birth: ")
        try:
            birthday=datetime.strptime(birthday_str, "%Y-%m-%d").date()
            return birthday
        except ValueError:
            print ("Invalid date")

def calculate_age_in_timedelta(birth_date):
    datetoday=datetime.now().date()
    age_in_timedelta=(datetoday-birth_date)
    return age_in_timedelta

def convert_minutes_to_words(total_minutes):
    p = inflect.engine()
    total_minutes_in_words = p.number_to_words(total_minutes)
    # Remove commas and "and"
    total_minutes_in_words = total_minutes_in_words.replace(",", "").replace(" and", "")
    return total_minutes_in_words

if __name__ == "__main__":
    main()
