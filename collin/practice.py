# class Student:
#     student_score = 95  # Class variable

#     def __init__(self, name):
#         Student.student_score += 10  # Increment the class variable
#         self.name = name  # Instance variable

#     def show(self):
#         print("Hi, my name is " + self.name)

# class Ricestudent(Student):
#     pass

# o1 = Ricestudent("Peter")  # Create an instance of Ricestudent
# #o2=Student("Emma")
# #o3=Ricestudent("John")
# #o4=Student("Jack")

# #o2.show()
# #print(o2.student_score)

# # o1.show()  # Call the show method
# print(o1.student_score)  # Access the class variable student_score

# # print(o3.student_score)
# # print(o4.student_score)

class Student:
    def __init__(self,first):
        self.__first = first
    def set_second(self, second):
        self.__second = second
o1= Student(1)
o2 = Student (2)
o3 = Student (4)
o2.set_second(3)
o3.third = 5
print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)
