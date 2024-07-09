# Base class Left
class Left:
    # Class attribute of Left
    var = "L"
    # Class attribute specific to Right
    var_left = "LL"
    # Method of the Left class
    def fun(self):
        return "Left"

# Base class Right
class Right:
    # Class attribute of Right
    var = "R"
    # Class attribute specific to Right
    var_right = "RR"
    # Method of the Right class
    def fun(self):
        return "Right"

# Sub class inheriting from both Left and Right
class Sub(Left, Right):
    # No additional attributes or methods
    pass

# Create an instance of Sub
obj = Sub()

# Print the attibutes and methods of the obj
print(obj.var, obj.var_left, obj.var_right, obj.fun())


"""
 The output of the program is:
 L, LL, RR, Left

obj.var: This attribute is found in both Left and Right classes. However, due to the MRO, the Left class’s var attribute ("L") is used.
obj.var_left: This attribute is specific to the Left class and is found directly.
obj.var_right: This attribute is specific to the Right class and is found directly.
obj.fun(): This method is found in both Left and Right classes. The MRO dictates that Left is checked before Right, so Left’s fun method is used.
"""
