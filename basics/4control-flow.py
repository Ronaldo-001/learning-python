print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
weight = int(input("what is your weight in cm?"))
if height>=180:
  print("you have right height")
  if weight<100:
    print("your weight is right")
    print("you can ride ")
  else:
    print("your weight is high ")
    print("you cant ride")
elif height<50:
  print("you height is too low")
else:
  print("you cant ride")

height = int(input("What is your height in cm? "))
weight = int(input("what is your weight in cm?"))
money=int(input("enter amount of money u have in $"))
if height>=180 and weight<=100:
  print("you can ride cause you have perfect height and weight")
if money>=1000 or height>=200:
  print("you should pay extra money for your height")
if money==0:
  print("no money no ride")