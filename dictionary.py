#to create dictionary
mydictionary={"name":"monkey","age":2}
print(type(mydictionary))
print(mydictionary)
print(mydictionary["age"])
#duplicates not allowed
mydictionary1={"name":"monkey","age":2,"age":3}
print(type(mydictionary1))
print(mydictionary1)
#dictionary length
print(len(mydictionary))
#dict() constructor
thisdict=dict(name="cat",age=2)
print(thisdict)
#get values
x=mydictionary.get("name")
print(x)
#get keys
y=mydictionary.keys()
print(y)
#get items
z=mydictionary.items()
print(z)
#adding items
mydictionary["colour"]="red"
print(mydictionary)
#copying a dictionary
thisdictionary=mydictionary.copy()
print(thisdictionary)
#nested dictionaries
mydict={"child1":{"name":"kali","year":2004},"child2":{"name":"centos","year":2006}}
print(mydict)
print(type(mydict))

output:
<class 'dict'>
{'name': 'monkey', 'age': 2}
2
<class 'dict'>
{'name': 'monkey', 'age': 3}
2
{'name': 'cat', 'age': 2}
monkey
dict_keys(['name', 'age'])
dict_items([('name', 'monkey'), ('age', 2)])
{'name': 'monkey', 'age': 2, 'colour': 'red'}
{'name': 'monkey', 'age': 2, 'colour': 'red'}
{'child1': {'name': 'kali', 'year': 2004}, 'child2': {'name': 'centos', 'year': 2006}}






