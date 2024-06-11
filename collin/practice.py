class Employee:
        def __init__(self,name,salary,project_satus):
                 self.name=name
                 self.salary=salary
                 self.project_status=project_status

        def print_time(self):
                print("Time is: ", self.hours, ":", self.minutes,":",self.seconds)

        def display_seconds(self):
                total_seconds=self.hours*3600+self.minutes*60+self.seconds
                print("Time in seconds is:", total_seconds)


obj1=Time(5,3,23)
obj1.print_time()
obj1.display_seconds()


