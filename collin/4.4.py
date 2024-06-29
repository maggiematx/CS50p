class A:
     # class attribute
     var = 1

     def __init__(self):
         # Instance attribute
         self.x = 1

# Child class
class B(A):
      def __init__(self):
            # call the parent class's __init__method
            super().__init__()

# b is another instance of calss B
b = B()


print(hasattr(A,"__init__"))

print(hasattr(B,"__init__"))

print(hasattr(b,"__init__"))

print(hasattr(b,"x"))

print(hasattr(A,"var"))

print(hasattr(b,"var"))

print(hasattr(B,"super"))

"""
The output of the program is:
True
True
True
True
True
True
False

1. hasattr(A, "__init__"):
This checks if the class A has an __init__ method.
Since A defines an __init__ method, this check will return True.

2. hasattr(B, "__init__"):
This checks if the class B has an __init__ method.
Since B defines an __init__ method, this check will return True.

3. hasattr(b, "__init__"):
This checks if the instance b has an __init__ method.
In Python, methods defined in the class (like __init__) are not directly stored in the instance; they are accessed through the class. However, hasattr will return True because b can access the __init__ method via its class.

4. hasattr(b, "x"):
This checks if the instance b has an attribute x.
The __init__ method of B calls the __init__ method of A via super().__init__(), which sets self.x = 1. So, b does have an attribute x.

5. hasattr(A, "var"):
This checks if the class A has an attribute var.
Since var is defined as a class attribute in A, this check will return True.

6. hasattr(b, "var"):
This checks if the instance b has an attribute var.
The instance b inherits the class attribute var from A, so this check will return True.

7. hasattr(B, "super"):
This checks if the class B has an attribute super.
super is a built-in function in Python and is not an attribute of the class B, so this check will return False.
"""
