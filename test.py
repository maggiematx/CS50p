
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
        print(f"The current time is ${self.seconds}")

def main():
    obj1 = Time()
    current_time=datetime.now()
    formatted_time=current_time.strftime("%H:%M:%S")
    Print("The current time is)

def convert_seconds():

    return  Time()


obj1.display_time()


