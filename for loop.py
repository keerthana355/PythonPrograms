          #Program-1
#Python program to print characters present in the given string
s="Twinkle Solutions"
for x in s:
 print(x)

'''Output:
T
w
i
n
k
l
e

S
o
l
u
t
i
o
n
s'''

          #Program-2
#Python program to print value present in the given list
fruits=["apple","banana","cherry"]
for x in fruits:
 print(x)

'''Output:
apple
banana
cherry'''

          #Program-3
#Python program to print "hello" 10 times
for x in range(10):
 print("hello")

'''Output:
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello'''
 
          #Program-4
##Python program to print first 10 natural numbers
for x in range(1,11):
 print(x) 

'''Output:
1
2
3
4
5
6
7
8
9
10'''

          #Program-5
#Python program to print half pyramid
rows = int(input("Enter the number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("\n")

'''Output:
Enter the number of rows: 7
A

B B

C C C

D D D D

E E E E E

F F F F F F

G G G G G G G'''

         #Program-6
#Python program to find factorial of a number
n=int (input ("Enter a number: "))
factorial=1
if n>=1:
    for i in range(1, n+1):
        factorial=factorial*i
print("Factorial of the given number is:",factorial)

'''Output:
Enter a number: 6
Factorial of the given number is: 720'''

        #Program-7
#Python program to check the given string is palindrome or not
x=str(input("Enter the string:"))
w=""
for i in x:
    w=i+w
if(x==w):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

'''Output:
Enter the string:malayalam
It is a palindrome'''

         #Program-8
for row in range(1,6):
  for col in range(1,6):
    print("*",end=" ")
  print()

'''output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *'''
          
