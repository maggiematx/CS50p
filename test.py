
from datetime import datetime

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def display_time(self):
        hours="5"
        minutes="33"
        seconds="45"
        return Time(hours, minutes, seconds)

def main():
    obj1 = Time()
    Print("The current time is display_time())

if __name__= "__main__":
    main()


