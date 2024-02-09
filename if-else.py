                          Program-1
#python program to get two number from the user and check whether the first number is less than second number or not
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
                       Program-2
#python program to check whether the given number is even or odd
a=intput("enter a number:")
if a%2==0:
 print("{} is even".format(a))
else:
 print("{} is odd".format(a))
  
'''output:
enter a number:6
given number is even'''
                       Program-3
#using and
a=10
b=20
c=30
if a>b and c<a:
 print("both conditions are true")
else:
 print("both conditions are false")

''' output:
both conditions are false

                      Program-4
#using or
a=10
b=20
c=5
if a>b or c<a:
 print("one condition is true")
else:
 print("no condition is true")

'''output:
one condition is true'''

                    Program-5
#using not
a=10
b=20
if not a>b:
 print("a is not greater than b")
else:
 print("a is greater than b")

'''output:
a is not greater than b'''

                     Program-6
#Python program to check whether a person is eligible to vote or not
age=int(input("Enter the age:"))
if age>=18:
  print("You are eligible to vote")
 else:
  print("You are not eligible to vote")

'''Output:
Enter the age:36
You are eligible to vote'''

                      Program-7
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

'''Output:
c is the largest number'''
