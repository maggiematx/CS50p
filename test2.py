def main():
    student = get_student()
    print(f"{student["name"]} from {student["house"]}")

def get_student():
    student={}
    student["name"]==input("name: ")
    student["house"]==input("house: ")
    return stduent

if __name__=="__main__":
    main()
