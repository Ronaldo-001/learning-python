#key-value pairs

# Dictionary creation
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Example of dictionary usage
print(my_dict['name'])  # Accessing value by key
print(my_dict.get('age'))  # Using get() method to access value

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print(my_dict)

# Iterating over keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if 'city' in my_dict:
    print("City key exists in the dictionary")

# Removing a key-value pair
removed_value = my_dict.pop('age')
print(f"Removed value: {removed_value}")
print(my_dict)
"""
dict[key]: Access value by key.
dict.get(key): Access value using get() method.
dict[key] = value: Add or update a key-value pair.
dict.items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
dict.keys(): Returns a view object that displays a list of all the keys in the dictionary.
dict.values(): Returns a view object that displays a list of all the values in the dictionary.
dict.pop(key): Removes the key and returns its value.
dict.clear(): Removes all elements from the dictionary.
len(dict): Returns the number of items in the dictionary.
"""

#passing dictionary as argument
def process_person(person):
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age', 'Age not specified')}")
  

# Example usage
person_info = {
    'name': 'Alice',
    'age': 25,
    'city': 'London'
}

process_person(person_info)

#my_dict.get('age') uses the get() method to retrieve the value associated with the key 'age'.
