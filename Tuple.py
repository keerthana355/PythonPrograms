#To create tuple
tuple=("apple","banana","cherry")
print(tuple)
#allows duplicates
tuple=("apple","banana","cherry","apple")
print(tuple)
#tuple length
print(len(tuple))
#one item tuple
tuple1=("apple,")
print(tuple1)
print(type(tuple))
#tuple can be any datatype
tuple3=("apple",4,True,12.3)
print(tuple3)
#access tuple
print(tuple[2])
#negative indexing
print(tuple3[-1])
#range
print(tuple[2:4])
#converting tuple into list to allow modifications 
mylist=list(tuple)
print(mylist)
print(type(mylist))

