              #Program-1
#Python program to demonstrate multi-level inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
#The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
#The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating bread")
d = DogChild()
d.bark()
d.speak()
d.eat()

'''OUTPUT:
og barking
Animal Speaking
Eating bread '''


                      #Program-2
class human:
 def __init__(self,num_heart):
  self.eyes=2
  self.num_heart=num_heart
 def work(self):
  print("I can work") 

class male(human):
 def __init__(self,name):
  self.name=name
 def lift(self):
  print("I can lift")
 def work(self):
  print("I can code")
 
class boy(male):
 def __init__(self,num_heart,name):
   human.__init__(self,num_heart)
   male.__init__(self,name)

 def work(self):
   #super().work() or
   human.work(self)
   male.work(self)
   print("I can test")

class programmer(boy):
    def work(self):
     human.work(self)
     print("I can program")

boy_1=boy("Ram",1)
boy_1.work()
print(boy.mro())
print(boy_1.name)
print(boy_1.num_heart)

'''Output:
I can work
I can code
I can test
[<class '__main__.boy'>, <class '__main__.male'>, <class '__main__.human'>, <class 'object'>]
1
Ram '''
