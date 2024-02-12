#Python program to demonstrate Hybrid inheritance
class Vehicle:
    def vehicle_info(self):
        print("Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Truck class")

# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("SportsCar class")

s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()

'''Output:
Vehicle class
Car class
SportsCar class '''