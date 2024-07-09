# Base class Top
class Top:
        # Method of the Top class
        def m_top(self):
                print("top")

# Middle_Left class inheriting from Top
class Middle_Left(Top):
        # Method of the Middle_Left class
        def m_middle(self):
                print("middle_left")

# Middle_Right class inheriting from Top
class Middle_Right(Top):
        # Method of Middle_Right class
        def m_middle(self):
             print("middle_right")

# Bottom class inehriting from both Middle_Left and Middle_Right
class Bottom(Middle_Left, Middle_Right):
        # Method of the Bottom class
        def m_bottom(self):
               print("bottom")

# Create an instance of Bottom
object = Bottom()
# Call the m_bottom method from the Bottom class
object.m_bottom()
# Call the m_middle method
object.m_middle()
# Call the m_top method from the Top class
object.m_top()

"""
The output of the program is:
bottom
middle_left
top

object.m_bottom() calls m_bottom from the Bottom class.
object.m_middle() calls m_middle from the Middle_Left class due to the MRO, which places Middle_Left before Middle_Right.
object.m_top() calls m_top from the Top class since neither Bottom nor Middle_Left nor Middle_Right override it.
"""

