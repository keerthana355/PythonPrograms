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
