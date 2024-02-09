#python program to get two number from the user and check first number is less than second number or not

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
if a<b:
 print(" a is less than b")
else:
 print("a is greater than b")
 
'''output:
enter the value of a:3
enter the value of b:7
a is less than b'''

#python program to check whether the given number is even or odd
a=intput("enter a number:")
if a%2==0:
 print("{} is even".format(a))
else:
 print("{} is odd".format(a))

'''output:
enter a number:6
given number is even'''

#using and
a=10
b=20
c=30
if a>b and c<a:
 print("both conditions are true")
else:
 print("both conditions are false")

#output:
both conditions are false

#using or
a=10
b=20
c=7
if a>b or c<a:
 print("one condition is true")
else:
 print("no conditions are true")

'''output:
one condition is true'''

#using not
a=10
b=20
if not a>b:
 print("a is not greater than b")
else:
 print("a is greater than b")

'''output:
a is not greater than b'''

#Python program to check whether a person is eligible to vote or not
age=int(input("Enter the age:"))
if age>=18:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")

'''Output:
Enter the age:36
You are eligible to vote'''
