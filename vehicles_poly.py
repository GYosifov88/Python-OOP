from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER_FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        summer_consumption = self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONSUMPTION
        if (summer_consumption * distance) <= self.fuel_quantity:
            self.fuel_quantity -= summer_consumption * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    AIR_CONDITIONER_FUEL_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        summer_consumption = self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONSUMPTION
        if (summer_consumption * distance) <= self.fuel_quantity:
            self.fuel_quantity -= summer_consumption * distance

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)
        return self.fuel_quantity


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
