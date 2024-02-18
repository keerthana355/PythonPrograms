#Built-in modules
#print(help("modules"))

import math
print(math.e)
print(math.pi)

'''Output:
2.718281828459045
3.141592653589793 '''

#importing user defined module

import My_module
print(My_module.a)
print(My_module.area_of_square(9))
print(My_module.calculator(3,5))

'''Output:
10
81
Addition is: 8
Subraction is: -2
Multiplication is 15
Division is: 0.6
None '''

#importing user defined module as shortcut name
import My_module as m
print(m.a)
print(m.area_of_square(7))
print(m.calculator(5,8))

'''Output:
10
49
Addition is: 13
Subraction is: -3
Multiplication is 40
Division is: 0.625
None '''
 
#importing particular function from our module
from My_module import a,calculator
print(a)
print(calculator(12,10))

'''Output:
10
Addition is: 22
Subraction is: 2
Multiplication is 120
Division is: 1.2
None '''

#importing all functions from user defined module
#from My_module import *
a=2
b=4
sum=a+b
print("value of a from another module",My_module.a)

'''Output:
value of a from another module 10 '''


