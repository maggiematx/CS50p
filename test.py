
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def display_time(self):
        print(f"Current time is ${self.seconds}")


    obj1 = Time("Maggie", 12345, 500)


    obj1.display_time()


