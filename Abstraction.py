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