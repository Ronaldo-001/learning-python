import math  # Import the math module

# Print all entities in the math module in alphabetical order
print(dir(math))

from random import random, seed  # Import random and seed functions from random module

# Generate and print 5 random float numbers between 0.0 and 1.0
for i in range(5):
    seed()  # seed() is called without any arguments, which uses the current system time to initialize the random number generator
    print(random())


print(math.sqrt(16))  # Calculate the square root of 16 using math.sqrt()
print(math.factorial(5))  # Calculate the factorial of 5 using math.factorial()

"""
when you call seed(3) in Python's random module, you are initializing the random number generator (RNG) with a specific seed value of 3. 
This means that the sequence of random numbers generated by subsequent calls 
to random functions will be deterministic and predictable as long as the same seed value (3 in this case) is use 
"""