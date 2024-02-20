# Python program demonstrate abstract base class work 
  
from abc import ABC,abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 40kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 23kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 26kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")                
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  

'''Output:
The mileage is 40kmph
The mileage is 27kmph
The mileage is 23kmph
The mileage is 26kmph '''


               #Program-2
from abc import ABC,abstractmethod
class vehicle(ABC):
 def __init__(self,n):
  no.of.tyres=n
 @abstractmethod
 def start(self):
  print("I can start")
 #normal method
 def display(self):
  print("non abstractclass") 

class bike(vehicle):
 def __init__(self):
  self.no_of_tyres=2
 def start(self):
  print("start with kick")

class scooty(vehicle):
 def __init__(self):
  self.no_of_tyres=2
 def start(self):
  print("self start")

class car(vehicle):
 def __init__(self):
  self.no_of_tyres=4
 def start(self):
  print("Start with key")

bike_1=bike()
bike_1.start()

scooty_1=scooty()
scooty_1.start()
print(scooty_1.no_of_tyres)


'''Output:
start with kick
self start
2 '''