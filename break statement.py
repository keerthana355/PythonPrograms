           #Program-1
#Python program to illustrate break statement
for i in range(1,10):
 if i==7:
  print("processing is enough")
  break
 print(i)

'''output:
1
2
3
4
5
6
processing is enough'''
  
           #Program-2
fruits=["apple","banana","cherry"]
for x in fruits:
 if x=="banana":
  break
 print(x)

'''Output:
apple'''


