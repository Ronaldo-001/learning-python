# Initialize a list with mixed data types
names = ["rock", "rick", "stan", 3, 4.4, "g"]
print(names)
print(len(names))  # Print the length of the list
print(names[2])  # Access the third element in the list

# Modify the list
names[2] = "stark"  # Change the third element
names.append("tommy")  # Add a new element at the end
names.insert(2, "penny")  # Insert an element at the third position, pushing the rest to the right
del names[-1]  # Remove the last element by index
names.remove("g")  # Remove the first occurrence of the value "g"
print(names)

# Sorting and reversing a list
numbers = [3, 5, 2, 1, 9]
numbers.sort()  # Sort the list in ascending order
print(numbers)
numbers = [3, 5, 2, 1, 9, "Hello"]
numbers.reverse()  # Reverse the list order
print(numbers)
numbers = [3, 5, 2, 1, 9]
print(max(numbers))  # Print the maximum value in the list
numbers.pop(3)  # Remove the element at the fourth position
print(min(numbers))  # Print the minimum value in the list
numbers.clear()  # Clear all elements from the list
print(numbers)

# Iterating through a list
team = ["sam", "ram", "john", "mary"]
for i in team:
    print(i)  # Print each element in the list
for i in team[1:2]:  # Print elements within the specified range of indices
    print(i)

# Swapping elements in a list
countries = ["India", "Italy", "USA"]
# Normal method
temp = countries[0]
countries[0] = countries[1]
countries[1] = temp
print(countries)

# Special swap in Python
countries = ["India", "Italy", "USA"]
countries[0], countries[1] = countries[1], countries[0]  # Swap the first and second elements
print(countries)

# List assignment and addressing
name = "Ricky"  # Here two variables point to different addresses
name2 = "Rock"
name_list = [1, 2, 3, 4]  # In lists, even though the list is assigned to another list, both lists point to the same address
name_list2 = name_list
name_list2.pop(3)  # Remove the fourth element from the list
print(name_list)

# Slicing in lists
letters = ["a", "b", "c", "d"]
print(letters[1:3])  # Slicing the list from index 1 to 2
del letters[1:3]  # Delete elements from index 1 to 2
letters = ["a", "b", "c", "d"]
letters2 = letters[:]  # Create a new list with the same elements but different address
letters2.clear()  # Clear all elements from the new list
print(letters)  # Original list not affected
print(letters2)  # New list is now empty

# Finding elements in a list using 'in' and 'not in'
score = ["good", "average", "excellent"]
print("good" in score)  # Check if "good" is in the list
print("addd" not in score)  # Check if "addd" is not in the list

# Nested lists - 2D example
matrix_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Iterating through a 2D list
for row in matrix_2d:
    for elem in row:
        print(elem, end=" ")
    print()

# Nested lists - 3D example (3x3 matrices)
matrix_3d = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]
# Iterating through a 3D list
for i in matrix_3d:
    for j in i:
        for elem in j:
            print(elem, end=" ")
        print()
    print()
    
print(matrix_3d[0][1][2])