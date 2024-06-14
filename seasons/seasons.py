from datetime import datetime, date
from num2words import num2words


class Age:
    def __init__(self,days, hours, minutes):
        self.days=days
        self.hours=hours
        self.minutes=minutes


    def display_minutes(self):
        total_minutes=self.days*24*60+self.hours*60+self.minutes
        return total_minutes


def main():
    birth_date=get_birthday()
    age_in_days=calculate_age_in_days(birth_date)
    age=Age(age_in_days, 0, 0)

    total_minutes=age.display_minutes()
    total_minutes_in_words=num2words(total_minutes).replace("-"," ")

    print("You are:", total_minutes, "mimutes old.")


def get_birthday():
    birthday_str=input("Date of Birth: ")
    try:
        birthday=datetime.strptime(birthday_str, "%Y-%m-%d").date()
        return birthday
    except ValueError:
        print ("Invalid date")

def calculate_age_in_days(birth_date):
    datetoday=date.today()
    age_in_days=(datetoday-birth_date).days
    return age_in_days

if __name__ == "__main__":
    main()
