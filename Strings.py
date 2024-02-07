a="hello, world"
print(a)
#multiline strings
b="""string is a sequence 
of characters surrounded single quotes 
or double quotes"""
print(b)
#accessin strings with index number
print(a[2])
#looping through a string
for x in "banana":
   print(x)
#string length   
print(len(a))
#check string
print("world" in a)
#slicing
print(a[2:5])
#slice from start
print(a[:5])
#slice to end
print(a[:])
#negative slicing
print(a[-5:-2])
#Strings built-in-methods
#uppercase
print(a.upper())
#lowercase
print(a.lower())
#remove whitespace
print(a.strip())
#replace string
print(a.replace("h","j"))
#split strings
print(a.split())
#string concatenation
x="hello"
y="world"
print(x+" "+y)
age=26
#string formatting
txt="my name is john, and my age is {}"
print(txt.format(age))

output:
hello, world
string is a sequence
of characters surrounded single quotes
or double quotes
l
b
a
n
a
n
a
12
True
hello   
hello, world
wor
HELLO, WORLD
hello, world
hello, world
jello, world
['hello,', 'world']
hello world
my name is john, and my age is 26
s
