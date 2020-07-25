from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    pass

m = Motorcycle(20, 200, 10)
print(m.default_fuel_consumption(20, 200))
print(m.drive(100))