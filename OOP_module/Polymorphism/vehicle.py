from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.__class__ is Truck:
            needed_fuel = (self.fuel_consumption + 1.6) * distance
            if self.fuel_quantity >= needed_fuel:
                self.fuel_quantity -= needed_fuel
        else:
            needed_fuel = (self.fuel_consumption + 0.9) * distance
            if self.fuel_quantity >= needed_fuel:
                self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        if self.__class__ is Truck:
            truck_tank = fuel * 0.95
            self.fuel_quantity += truck_tank
            return
        self.fuel_quantity += fuel


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        Vehicle.__init__(self, fuel_quantity, fuel_consumption)


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        Vehicle.__init__(self, fuel_quantity, fuel_consumption)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
