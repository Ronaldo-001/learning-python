class Person:
    # Constructor to initialize first_name and last_name attributes
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Method to print a simple greeting
    def hi(self):
        print("Hello")

    # Method to print the person's details
    def details(self):
        print(f"I am {self.first_name} {self.last_name}")
        result = 5  # Local variable, not accessible outside this method
    
class Agent(Person):
    # Constructor to initialize first_name, last_name, and code attributes
    def __init__(self, first_name, last_name, code):
        # Initialize the inherited attributes using the parent class constructor
        Person.__init__(self, first_name, last_name)  # super().__init__(first_name, last_name) is also fine
        self.code = code

    # Overriding the details method to include the agent's code
    def details(self):
        # Print the agent's specific details without calling the parent class method
        print(f"I am an Agent. My name is {self.first_name} {self.last_name} with code {self.code}")

    def call_parent_method(self):
        super().details() #just call parent method but the variable values are overriden by Agent class

# Create an instance of Person
obj1 = Person("Ethan", "Hunt")
obj1.hi()         # Output: Hello
obj1.details()    # Output: I am Ethan Hunt

# Create an instance of Agent
obj2 = Agent("Athena", "Fox", 102)
obj2.hi()         # Output: Hello
obj2.details()    # Output: I am an Agent. My name is Athena Fox with code 102
obj2.call_parent_method() #output: I am Athena Fox
