class Circle:
    pi = 3.14

    def __init__(self, radius=1):  # default radius = 1 if not passed
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def double_radius(self):
        self.radius *= 2  # methods in class can access and modify attributes of an instance

    def mul_radius(self, num):
        result = self.radius * num
        return result  # here result and num are accessible only by this method inside the class

# Create an instance of Circle with radius 10
obj = Circle(10)

# Output: Area of the circle with radius 10 (pi * r^2)
print(obj.area())  # Output: 314.0

# Double the radius using the double_radius method
obj.double_radius()

# Output: New radius after doubling (10 * 2)
print(obj.radius)  # Output: 20

# Multiply the radius by 5 using the mul_radius method
# Output: Result of multiplying current radius (20) by 5
print(obj.mul_radius(5))  # Output: 100
