#legal variables
myvar=10
my_var=10
_my_var=10
myvar2=10
myVar=10
MYVAR=10
print(myvar)
print(my_var)
print(_my_var)
print(myvar2)
print(myvar2)
print(MYVAR)
#illegal variables
#2myvar=10
#my-var==10
#my$var=10
#for=10
#my var=10
#Multi words variable names
#camel case
myVariableName=10
print(myVariableName)
#pascal case
MyVariableName=10 
print(MyVariableName)
#snake case
my_variable_name=10
print(my_variable_name)
#multiple values to mutilpe variables
x,y,z=10,20,30
print(x,y,z)
#one value to multiple variables
x=y=z=20
print(x,y,z)
#global variables
x="awesome"
def myfunc():
  print("python is"+x)
myfunc()
#....................
x="easy"
def myfunc():
    x="fantastic"
    print("python is"+x)
myfunc()
print("python is"+x)