# Python example to show the working of multiple inheritance
class Employee:
        pass
class Person1(Employee):
	def __init__(self):
		self.name1="Ram"
		print("Person1")
class Person2(Employee):
	def __init__(self):
		self.str2="Sita"
		print("Person2")
class Derived(Person1, Person2):
	def __init__(self):
		Person1.__init__(self)
		Person2.__init__(self)
		print("Derived")
        def printname(self):
		print(self.name1,self.name2)
emp=Derived()
emp.printname()

'''Output:
Person1
Person2
Derived
Ram Sita '''


