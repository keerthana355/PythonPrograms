#python program to get two number from the user and check first number is less than second number or not

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
if a<b:
 print(" a is less than b")
else:
 print("a is greater than b")

#python program to check whether the given number is even or odd
a=int(input("enter a number"))
if (a%2)==0:
 print("{} is even".format(a))
else:
 print("{} is odd".format(a))

#using and
a=10
b=20
c=30
if a>b and c<a:
 print("both conditions are true")
else:
 print("both conditions are false")

#using or
a=10
b=20
c=5
if a>b or c<a:
 print("one condition is true")
else:
 print("no condition is true")

#using not
a=10
b=20
if not a>b:
 print("a is not greater than b")
else:
 print("a is greater than b")

#Python program to check whether a person is eligible to vote or not
age=int(input("Enter the age"))
if age>=18:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")

#Python program to find the largest number of the given three numbers
a=19
b=30
c=100
if a>b and a>c:
  print("a is the largest number")
if b<a and b>c:
  print("b is the largest number")
if c>a and c>b:
  print("c is the largest number")
