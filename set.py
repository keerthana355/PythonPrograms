#To create a set
myset={"cat","dog","monkey"}
print(type(myset))
print(myset)
#don't allow dulplicates
set1={"dog","cat",1,True,"dog"}
print(set1)
#length of set
print(len(set1))
#set() constructor
thisset=set((3,4,6,7,8,0))
print(thisset)

output:
<class 'set'>
{'cat', 'monkey', 'dog'}
{1, 'cat', 'dog'}
3
{0, 3, 4, 6, 7, 8}
