class Employee:

    def __init__(self,name,salary=0,project_status):
                 self.name=name
                 self.salary=salary
                 self.project_status=project_status

    def check_status(self):
         if self.project_status=="complete":
              self.salary *= 1.10
         else:
              print(f"{self.name} is fired!")

def main():
    obj1 = get_status()
    obj1.check_status()

    if obj1.salary>0:
        print(f"{obj1.name}'s new salary is {obj1.salary:.2f}")
    else:
         print(f"{obj1.name} is fired!")

def get_status():
    name=input("Name: ")
    salary=int(input("Salary: "))
    status=input("Status: ")

    return Employee(name,salary,status)

if __name__== "__main__":
    main()

