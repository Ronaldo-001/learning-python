"""
print() # Print method is predefined and can be formatted with its own string format.
len()    # Len method is predefined and can be formatted with its own length.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.pages = pages
        self.author = author
    
    def __str__(self):
        """
        Return a string representation of the Book object.
        This method is automatically called when using print() on an instance of Book.
        """
        return f"The Book \"{self.title}\" was written by {self.author}"

    def __len__(self):
        """
        Return the length of the Book object, which is defined as the number of pages.
        This method is automatically called when using len() on an instance of Book.
        """
        return self.pages

# Create an instance of Book
obj = Book("How to Do Something", "Rock", 120)

# Print the string representation of the Book object using __str__ method
print(obj)  # Output: The Book "How to Do Something" was written by Rock

# Get the length of the Book object using __len__ method
print(len(obj))  # Output: 120
