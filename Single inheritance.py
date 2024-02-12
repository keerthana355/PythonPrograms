#Python program to demonstrate Single inheritance
class Vehicle:
    def Vehicle_info(self):
        print('Vehicle class')
class Car(Vehicle):
    def car_info(self):
        print('Car class')
car = Car()
car.Vehicle_info()
car.car_info()

'''Output:
Vehicle class
Car class '''