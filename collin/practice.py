class Time:
        def __init__(self,hours, minutes, seconds):
                 self.name=hours
                 self.salary=minutes
                 self.project_status=seconds

        def display_time():
                total_seconds=hours*3600+minutes*60+seconds

obj1=Time(5,3,23)
print 
obj1.display_time()


