                  Program-1
#Python program to demonstrate nested if statement
a=99
if a<100:
   print("a is less than 100")
   if a%2==0: 
         print("a is even")
   else:
         print("a is odd")
else:
 print("a is greater than 100")

'''Output:
a is less than 100
a is odd'''
                 Program-2
#Python program to check the given number is divisible by 2 and 3
num=59
if num%2==0:
   if num%3==0:
      print("Divisible by 2 and 3")
   else:
      print("Divisible by 2 and not divisble by 3")
else:
    if num%3==0:
      print("Divisible by 3 and not divisble by 2")
    else:
      print("Not divisble by 2 and and not divisble by 3")

'''Output:
Not divisble by 2 and and not divisble by 3'''
   
