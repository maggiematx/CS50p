class Employee:

    def __init__(self,name,salary,project_status):
                 self.name=name
                 self.salary=salary
                 self.project_status=project_status


def main():
    obj1 = get_status()
        if obj.status == "complete":
            return salary * (1+0.1)

        else:
            print(f"{obj1.name} is fired!")


def get_status():
    name=input("Name: ")
    salary=int(input("Salary: "))
    status=input("Status: ")

    return Employee(name,salary,status)

if __name__== "__main__":
    main()

