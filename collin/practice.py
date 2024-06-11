class Employee:
        def __init__(self,name,salary,project_status):
                 self.name=name
                 self.salary=salary
                 self.project_status=project_status

        def final_status(self):
                if self.project_status=="complete":
                        print(f"{self.name} receives 10% pay rise!")
                else:
                        print(f"{self.name} is fired!")


obj1=Employee("Maggie", "$4000", "complete")
obj2=Employee("kevin", "$3000", "incomplete")
obj1.final_status()
obj2.final_status()


