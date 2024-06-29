class ExampleClass:
    def __init__(self, val):
        # If the value is odd, set attribute 'a' to 1
        if val % 2 != 0:
            self.a = 1
        # If the value is even, set attribute 'b' to 1
        else:
            self.b = 1

# Create an instance of ExampleClass with val = 1
example_object = ExampleClass(1)

# Print the value of attribute 'a'
print(example_object.a)

# Print the value of attribute 'b'
print(example_object.b)

"""The output of the program is:
1
AttributeError: 'ExampleClass' object has no attribute 'b'

Inside the __init__ method, the condition if val % 2 != 0 is checked. Since 1 is odd (1 % 2 != 0 is True), the attribute self.a is set to 1. The attribute self.b is not set because the else block is not executed."""

