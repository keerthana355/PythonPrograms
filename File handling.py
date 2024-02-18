#read mode
f=open("file1.txt","r")
data=f.read()
print(data) 

'''Output:
hi welcome.I will complete it in 20 days
I want to become expert in python'''

#or
f=open("file1.txt")
print(f.read())

'''Output:
hi welcome.I will complete it in 20 days
I want to become expert in python'''

#Read the first 5 characters of file
f=open("file1.txt")
print(f.read(5))

#Output:
hi we

#to read one line from the file
f=open("file1.txt")
print(f.readline())

'''Output:
hi welcome.I will complete it in 20 days '''

#to read two lines from the file
f=open("file1.txt",'r')
print(f.readline())
print(f.readline())

'''Output:
hi welcome.I will complete it in 20 days
I want to become expert in python'''

#read mode using for loop
f=open("file1.txt","r")
for x in f:
  print(x)

'''Output:
hi welcome.I will complete it in 20 days
I want to become expert in python

#write mode
f=open("file1.txt","w")
(f.write("I am learning python programming."))

'''Output:
I am learning python programming. '''

#r+ mode
f=open("file1.txt","r+")
print(f.read())
f.write("I will complete it in 20 days") 

'''Output:
I am learning python programming.
I am learning python programming.I will complete it in 20 days '''

#w+ mode
f=open("file1.txt","w+")
f.write("hi welcome")
f.seek(0)
print(f.read())
f.close()

'''Output:
hi welcome '''

#a mode
#f=open("file1.txt","a")
#f.write("I want to become expert in python")

'''Output:
hi welcomeI want to become expert in python '''


#a+ mode
f=open("file1.txt","a+")
f.write("I want to become expert in python")
f.seek(0)
print(f.read())

'''Output:
hi welcomeI want to become expert in pythonI want to become expert in python '''
