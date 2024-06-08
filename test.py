
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
    time=get_time()
    total_seconds=time.display_time()
    print("The current time is: ", time.hours, ":", time.minutes, ":", time.seconds)
    print("The current time is: ", total_seconds)

def get_time():
    current_datetime=datetime.now()

    hours=current_datetime.hour
    minutes=current_datetime.minute
    seconds=current_datetime.second

    return Time(hours,minutes,seconds)


if __name__== "__main__":
    main()


