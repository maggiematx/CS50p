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
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
