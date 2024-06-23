my_tuple=(1,"hello",3.33,55)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[1] -- nothing works
#mytuple.append(3) -- attribute error nothing works cause tuple is immutable

#we can slice it like list
print(my_tuple[1:3])

nested_tuple=((1,2),("name","age"))
print(nested_tuple[0][1]) # nested tuple access 

#passing tuple as argument in function that has multiple arguments
def my_function(args,*argd):
    print(type(args))
    print(args)
    print(type(argd))
    print(argd)
    
my_function("stored in args","stored in *argd 1","stored in argd 2")