
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def print_time(self):
        print(self.hours,self.minutes,self.seconds)
    def convert(self):
        second1=3600*self.hours
        second2=self.minutes*60
        secondsfial=second1+second2+self.seconds

t=Time(10,10,00)
t.print_time()
t.convert()
