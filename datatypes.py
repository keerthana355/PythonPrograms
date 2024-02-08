a="hello world" #string
print(type(a))
b=20 #integer
print(type(b))
c=20.5 #floating point
print(type(c))
d=2+4j #complex
print(type(d))
e=["apple","banana","cherry"] #list
print(type(e))
f=("apple","banana","cherry") #tuple
print(type(f))
g={"name":"john","age":36} #dict
print(type(g))
h=range(6) #range
print(type(h))
i=True #boolean
print(type(i))
j=b"hello" #bytes
print(type(j))
k=bytearray(5) #bytesarray
print(type(k))
l=memoryview(bytes(5)) #memoryview
print(type(l))
m=None #None
print(type(m))
n={"apple","banana","cherry"}
print(type(n))
o=frozenset({"apple","banana","cherry"})
print(type(o))

output:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'range'>
<class 'bool'>
<class 'bytes'>
<class 'bytearray'>
<class 'memoryview'>
<class 'NoneType'>
<class 'set'>
<class 'frozenset'>
