# Modules

# Math module - functions of math
import math  # Import the math module

print(math.sin(90))  # Calculate sine of 90 degrees using math module's sin function
print(math.pi)  # Print the value of pi from the math module

# Importing multiple modules
# import math, sys  # You can import multiple modules like math and sys

# Importing specific entities from modules
# from math import pi  # Importing only the constant pi from the math module

# Importing with aliasing
# import math as m  # Importing math module with alias m
# from math import pi as p, sin as s  # Importing pi as p and sin as s from math module

from math import pi as p, sin as s  # Import pi as p and sin as s from math module

print(p)  # Print the value of pi using alias p
print(s(90))  # Calculate sine of 90 degrees using alias s for sin function from math module
