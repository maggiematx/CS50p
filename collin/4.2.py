class Classy:
    # Class attribute
    varia = 1

    def __init__(self):
        # Instance attribute
        self.var = 2

    def method(self):
        # Instance method (does nothing in this example)
        pass

    def __hidden(self):
        # Name mangling private method
        pass

# Create an instance of Classy
obj = Classy()

# Print the dictionary of instance attributes
print(obj.__dict__)

# Print the dictionary of class attributes, methods
print(Classy.__dict__)

""" The output of the program is:
{'var': 2}
{
    '__module__': '__main__',
    'varia': 1,
    '__init__': <function Classy.__init__ at 0x7e0d15cf16c0>,
    'method': <function Classy.method at 0x7e0d15cf18a0>,
    '_Classy__hidden': <function Classy.__hidden at 0x7e0d15cf2700>,
    '__dict__': <attribute '__dict__' of 'Classy' objects>,
    '__weakref__': <attribute '__weakref__' of 'Classy' objects>,
    '__doc__': None
}

obj.__dict__ shows only the instance-specific attributes ({'var': 2}).
Classy.__dict__ shows all class-level attributes, methods, and other metadata, including class attributes (varia), methods (method, __hidden), and internal attributes. """
