class Employee:

    def __init__(self,name,salary,project_status):
                 self.name=name
                 self.salary=salary
                 self.project_status=project_status

    def check_status(self):
         if self.project_status=="complete":
              self.salary *= 1.10
         else:
              self.salary=0

def main():
    employee= get_status()
    employee.check_status()

    if employee.salary>0:
        print(f"{employee.name}'s new salary is {employee.salary:.2f}")
    else:
         print(f"{employee.name} is fired!")

def get_status():
    name=input("Name: ")
    salary=int(input("Salary: "))
    status=input("Status: ").lower().strip()

    while status not in ["complete", "incomplete"]:
         status=input("Status: ").lower().strip()


    return Employee(name,salary,status)

if __name__== "__main__":
    main()

