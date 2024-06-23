class Employee():

    company="amazon" # class object attribute accessed by all instances of a class and object

    def __init__(self,name,age):
        self.name=name
        self.age=age

object=Employee("ronaldo",12)
print(object.age)
print(object.name)
print(object.company)
print(f"The employee {object.name} of age {object.age} is working at {object.company}")

object.age=18
print(object.age) # update the class attribute

# company is a class attribute, meaning it's shared by all instances of the employee class.
# name and age are instance attributes, unique to each instance of employee.
# The __init__ method initializes the instance attributes when an employee object is created.\

# The self keyword is used in Python to represent the instance of the class. It allows access to the attributes and methods of the class in object-oriented programming. Here’s why self is essential:

# Distinguishing between Class and Instance Attributes:

# self.name and self.age are instance attributes, unique to each instance of the Employee class. Using self ensures that these attributes are tied to the specific instance.
# Without self, Python would not know whether you are referring to a class attribute, a global variable, or something else.

# Accessing Instance Attributes and Methods:

# self is used to access instance attributes and methods within the class. It allows you to refer to the instance’s variables and methods.

# Instance-specific Data:

# self allows each instance to maintain its own data. For example, each Employee object can have different name and age values.
