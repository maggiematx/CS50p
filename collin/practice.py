class Time:
        def __init__(self,hours, minutes, seconds):
                 self.hours=hours
                 self.minutes=minutes
                 self.seconds=seconds

        def display_time(self):
                total_seconds=self.hours*3600+self.minutes*60+self.seconds
                print("Time in seconds is: ", total_seconds)



obj1=Time(5,3,23)

obj1.display_time()


