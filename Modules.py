#Built-in modules
#print(help("modules"))

import math
print(math.e)
print(math.pi)

#importing user defined module

import My_module
print(My_module.a)
print(My_module.area_of_square(9))
print(My_module.calculator(3,5))

#importing user defined module as shortcut name
import My_module as m
print(m.a)
print(m.area_of_square(7))
print(m.calculator(5,8))
 
#importing particular function from our module
from My_module import a,calculator
print(a)
print(calculator(12,10))

#importing all functions from user defined module
#from My_module import *
a=2
b=4
sum=a+b
print("value of a from another module",My_module.a)



