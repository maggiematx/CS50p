# class Person:
#     def __init__(self, name, age):  # Fixed typo in method name
#         self.__name = name
#         self.__age = age

#     def get_name(self):  # Corrected method definition and indentation
#         return self.__name

#     def set_name(self, name):  # This should set a new name, not return the old name
#         self.__name = name

#     def get_age(self):  # Corrected method definition and indentation
#         return self.__age

# # Creating an instance of Person
# p = Person("John", 30)

# p. __name="ma"

# Accessing the private attribute using name mangling
# print(p._Person__name)  # Corrected typo in the print statement

class A:
    def __init__(self, a=1):
        self.__var =a


p(A)
