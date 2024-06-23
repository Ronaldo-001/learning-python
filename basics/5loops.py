#Loops 
#for loop 
fruits=["Apple","Peach","Pear"] #list 
for fruit in fruits: #fruit variable loops through each fruits 
  print(fruit)         #fruit=apple.. in list
  print(fruit  +" "+"pie")


#for loop with range() function

# for number in range(a,b): //syntax
  # print(number)
for number in range(3): # here range-0,1,2 (n-1)
  print(number)
for number in range(1,10): # !!!range 10 always n-1
  print(number)

for number in range(1,11): # !!!range 10 always n-1
  print(number)
for number in range(1,11,3): # !here 3 is step skips3,6,..
  print(number)

# add all num from 1 to 100:
total=0
for number in range(1,101):
  total+=number
print(total)

for x in range(6):
  if x == 3: 
    break #get out of the loop
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: 
    continue #skip the number in the loop
  print(x)
else:
  print("Finally finished!")
  



#while loop
"""
while(True):
  execute condition until False
  """
total=0
i=0
while(i<=100):
  total+=i
  i+=1
print(total)

secret=3
guess=int(input("enter a number\n"))
while guess!=secret:
  guess=int(input("enter another number\n"))
  
  


#use for loop when limit is known and while loop for the rest and infinite