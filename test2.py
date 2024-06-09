from datetime import datetime

class Time:

    def __init__(self,hours,minutes,seconds):
                 self.hours=hours
                 self.minutes=minutes
                 self.seconds=seconds

    def diplay_seconds(self):
        total_seconds=hours*3600+minutes*60+seconds
        return total_seconds


def main():
    obj1 = get_time()
    total_seconds=obj1.display_seconds()
    print("The current time is: ", obj1.hours, ":", obj1.minutes, ":", obj1.seconds)
    print("The current time is: ", total_seconds)

def get_time():
    timenow=datetime.now()
    hours=timenow.hour
    minutes=timenow.minute
    seconds=timenow.second

    return Time(hours,minutes,seconds)

if __name__== "__main__":
    main()

