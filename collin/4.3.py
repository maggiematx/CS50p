class student:
      # Class attributes
      name = "John"
      age = "18"

      def __init__(self):
          # Instance attribute
          self.address = "plano"

# Check if the class 'student' has an attribute 'name'
print("student has name: ", hasattr(student,"name"))

# Check if the class 'student' has an attribute 'age'
print("student has age: ", hasattr(student,"age"))

# Check if the class 'student' has an attribute 'address'
print("student has address: ", hasattr(student,"address"))

""" The output of the program is:
student has name:  True
student has age:  True
student has address:  False

The hasattr function is used to check if an object has a specific attribute.
Class attributes name and age are accessible directly from the class and return True.
Instance attribute address is only accessible from an instance of the class and returns False when checked on the class itself."""
