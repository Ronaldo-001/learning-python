from mymodule import myfun,Myclass
from mypackages.mysubmodule import message

myfun() # calls the method defined in mymodule.py and also pycache generated to fast access next time
obj=Myclass("Hello") # access class method defined in mymodule.py
message() # acess package mypackages and inside file mysubmodule

#other way to add or import package and file
#import sys import path
# path.append("mypackages")
# now python knows mypackages is a py packages without __init__.py