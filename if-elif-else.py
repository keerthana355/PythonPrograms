                 Program-1
# Simple python program to understand if-elif-else
num=20
if num==10:
  print("given number is 10")
elif num==50:
  print("given number is 50")
elif num==100:
  print("given number is 100")
else:
  print("given number is not equal to 10,50,100")

'''Output:
given number is not equal to 10,50,100'''

                Program-2
#Python program to calculate the grade of a student
marks=int(input("Enter the marks:"))
if marks>85 and marks<=100:
 print("Congrats! your grade is A")
elif marks>65 and marks<=85:
 print("Your grade is B+")
elif marks>45 and marks<=65:
 print("Your grade is B")
elif marks>30 and marks<=45:
 print("Your grade is C")
else:
 print("Sorry! you are fail")

'''Output:
Enter the marks:99
Congrats! your grade is A'''
