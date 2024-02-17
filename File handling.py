#read mode
f=open("file1.txt","r")
data=f.read()
print(data) 
#or
f=open("file1.txt")
print(f.read())

#Read the first 5 characters of file
f=open("file1.txt")
print(f.read(5))

#to read one line from the file
f=open("file1.txt")
print(f.readline())

#to read two lines from the file
f=open("file1.txt",'r')
print(f.readline())
print(f.readline())

#read mode using for loop
f=open("file1.txt","r")
for x in f:
  print(x)

#write mode
f=open("file1.txt","w")
(f.write("I am learning python programming."))

#r+ mode
f=open("file1.txt","r+")
print(f.read())
f.write("I will complete it in 20 days") 

#w+ mode
f=open("file1.txt","w+")
f.write("hi welcome")
f.seek(0)
print(f.read())
f.close()

#a mode
#f=open("file1.txt","a")
#f.write("I want to become expert in python")


'''a+ mode
f=open("file1.txt","a+")
f.write("I want to become expert in python")
f.seek(0)
print(f.read())'''



