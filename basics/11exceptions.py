def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Division result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    else:
        print("No exceptions occurred.")
    finally:
        print("Execution of try-except block is complete.\n")

# Examples to invoke the function with different inputs
divide_numbers(10, 2)  # Normal division
divide_numbers(10, 0)  # Division by zero
divide_numbers(10, '2')  # Type error
divide_numbers(10, [])  # Generic exception



def safe_divide(a, b):
    try:
        result = a / b
        print(f"Division result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operand type(s) for division!")
    except:
        print("Unexpected error occurred!")

# Example usage
safe_divide(10, 2)  # Normal division
safe_divide(10, 0)  # Division by zero
safe_divide(10, '2')  # Type error
safe_divide(10, [])  # Generic exception


# In the safe_divide function provided, the except: block without specifying any exception
# type acts as a catch-all for any unexpected errors that occur during the execution of the try block. 
"""
The except: block at the end of the safe_divide function is useful for catching any unexpected exceptions 
that were not explicitly handled by the preceding except blocks (ZeroDivisionError and TypeError). 
It ensures that even if an unknown error occurs during the execution of the try block,
the program can provide a fallback response or handle it gracefully without crashing. 
This approach is beneficial for robust error handling in Python programs.
"""