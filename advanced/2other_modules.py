import platform  # Import the platform module
import sys       # Import the sys module
import random    # Import the random module

# Display some platform information
print(f"Python Version: {platform.python_version()}")  # Print Python version
print(f"Platform: {platform.platform()}")              # Print platform and it's version
print(f"System: {platform.system()}")                  # Print system
print(f"Processor: {platform.processor()}")            # Print processor

# Display some sys information
print(f"Python executable: {sys.executable}")          # Print Python executable path
print(f"Python path: {sys.path}")                      # Print Python path
print(f"Platform: {sys.platform}")                     # Print platform from sys module

# Generate and print 5 random integers between 1 and 100
print("Random Numbers:")
for _ in range(5):
    print(random.randint(1, 100))

# Additional use of random module to shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled List:", my_list)
