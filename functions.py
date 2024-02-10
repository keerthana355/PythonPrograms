           #Program-1
#Python program to illustrate functions
def my_fun():
 print("Hello world")
my_fun()

          #Program-2
#Python program to illustrate arguments in functions
def arg(animal):
 print(animal)
arg("tiger")
arg("lion")
arg("bear")

          #Program-3
#Python program to illustrate  arbitrary arguments(*args) in functions
def fun(*numbers):
  print("The lowest number is",numbers[0])
fun(0,1,2,3,4,5)

          #Program-4
#Python program to illustrate  keyword arguments in functions
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "sita", child2 = "gita", child3 = "rita")

         #Program-5
#Return statements
def my_function(x):
  return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))

         #Python-6
#pass statement
def my_function(x):
 pass

         #Python-7
#Python program to find the sum of two numbers
def sum(a,b):
 return a+b
print(sum(2,4))  

        #Program-8  
#Python program to check the given number is even or odd
def fun(x):
   if(x%2==0):
     print("even")
   else:
     print("odd")
fun(9)
fun(10)

        #Program-9
#Python program to find the square of a number
def square(num):    
    return num**2            
print(square(99)) 
       
        #Program-9
#Python program to illustrate nested functions  
def f1():
    s='hello world'
    def f2():
        print(s)
    f2()
f1()
 
         #Program-10
#Python program to illustrate recursive functions 
#To find factorial of a given number
def factorial(n):
    if n==0:  
        return 1
    else:
        return n*factorial(n-1) 
print(factorial(8))        
 
        #Program-11         
#Python program to check the number is prime or not using recursion
def Prime(n,i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return Prime(n,i+1)
if Prime(667):
    print(667,"is Prime")
else:
    print(667,"is not a Prime")


