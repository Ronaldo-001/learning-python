def function():
    print("hi.Im a function")

function() #call function

#function with arguments
def print_names(name1,name2):
    print("First Name is "+name1+"Last Name is: "+name2)
print_names("Rock","Star")


# pass arguments in predefined manner but("rock",name1="Star")-->error
def print_names(name1,name2):
    print("First Name is "+name1+"Last Name is: "+name2)
print_names(name2="Rock",name1="Star") 

#scope-local variable and global variable
#variables declared inside function cannot be accessed outside it 
#so we can declare global variable - but the changes in global variable only present inside function

#global variable cost
cost=50

def change():
    cost=45
    print(cost)
change()

print(cost)

#global variable inside a function (global keyword)

def fruits():
    global red 
    red="apple"
    print(red)

fruits()
print(red)

#RETURN in a function

def returning_function(name,age):
    return (f"your age is:{age}, your name is:{name}")
a=returning_function("sam",23) # return a string to a from the function
print(a)

#passing list as argument
def function(list):
    for i in list:
        print(i,end=" ") #print on same line
function(["richard","sam","ram"])

print()

#passing tuple as argument
def function(*tuple):
    for i in tuple:
        print(i,end=" ") #print on same line
function("rock",3,5.66)

#list and tuple points to same address 
def modify_list(input_list):
    print(f"Inside modify_list function - Initial memory address: {id(input_list)}")
    input_list.append(4)  # Modifying the list
    print(f"After modification - Memory address: {id(input_list)}")
    print(f"Modified list: {input_list}")

print()
# Example usage
my_list = [1, 2, 3]
print(f"Original list - Memory address: {id(my_list)}")
modify_list(my_list)
print(f"Outside function - Memory address: {id(my_list)}")
print(f"Original list outside function: {my_list}")

print("\n")

#tuple 
def modify_tuple(input_tuple):
    print(f"Inside modify_tuple function - Initial memory address: {id(input_tuple)}")
    # Trying to modify the tuple (which is not possible in Python)
    # So we create a new tuple by concatenating with another tuple
    input_tuple += (4,)
    print(f"After 'modification' - Memory address: {id(input_tuple)}")
    print(f"Modified tuple: {input_tuple}")

my_tuple = (1, 2, 3)
print(f"Original tuple - Memory address: {id(my_tuple)}")
modify_tuple(my_tuple)
print(f"Outside function - Memory address: {id(my_tuple)}")
print(f"Original tuple outside function: {my_tuple}")



