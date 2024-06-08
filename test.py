
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
    obj1 = Time()
    current_datetime=datetime.now()
    formatted_datetime = current_time.strftime("%H:%M:%S")
    Print("The current time is formatted_datetime")
    Print("The current time is display_time(formatted_datetime)")

def Time():
    hours=formatted_datetime[H]
    minutes=formatted_datetime[M]
    seconds=formatted_datetime[S]
    return Time(hours, minutes, seconds)


if __name__== "__main__":
    main()


