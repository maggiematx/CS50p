class Time:
        def __init__(self,hours, minutes, seconds):
                 self.hours=hours
                 self.minutes=minutes
                 self.seconds=seconds

        def display_time():
                total_seconds=hours*3600+minutes*60+seconds
                print("Time in seconds is: ", total_seconds)

obj1=Time(5,3,23)

obj1.display_time()


