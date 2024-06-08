
from datetime import datetime

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def display_time(self):
        total_seconds=self.hours*3600+self.minutes*60+self.seconds
        return total_seconds

def main():
    Time=get_time()
    Print("The current time is current_time")
    Print("The current time is display_time(current_time)")

def get_time():
    current_datetime=datetime.now()

    hours=current_datetime.hour
    minutes=current_datetime.minutes
    seconds=current_datetime.seconds

    current_time=get_time(hours,minutes,seconds)


if __name__== "__main__":
    main()


