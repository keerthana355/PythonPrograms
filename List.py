#to create a list
list1=["apple","grapes","guava","cherry","banana"]
print(list)
#allow duplicates
mylist=[2,5,9,8,9,2,4,4]
print(mylist)
#list length
print(len(list1))
print(len(mylist))
#list contain different datatypes
list2=(1,"apple",True,False)
print(list2)
#type()
print(type(list1))
#list() constructor
thislist=list(("apple","cherry","banana"))
print(thislist)
#to print the first value
print(list1[0])
#negative indexing
print(list1[-1])   #to print last element
#Range of indexes
print(list1[2:5])
print(list1[:5])
print(list1[1:])
#change item value
list1[1]="pomegranate"
print(list1)
print(list1[1])
#append() method
list1.append("orange")
print(list1)
#insert() method
list1.insert(1,"strawberry")
print(list1)
#extend() method
list3=["dog","cat","monkey"]
list4=["rose","lilly","jasmine"]
list3.extend(list4)
print(list3)
list4.extend(list3)
print(list4)
#remove() method
list4.remove("lilly")
print(list4)
#pop() method
list4.pop(1)
print(list4)
#delete 
del list4
#clear
list1.clear()
print(list1)
#copy method
ls1=[1,2,3,4],
ls2=[5,6,7,8]
ls1=ls2.copy()
print(ls1)