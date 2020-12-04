from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.__class__._INCREASED_FUEL) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel

    @property
    @abstractmethod
    def _INCREASED_FUEL(self):
        return self._INCREASED_FUEL


class Car(Vehicle):
    _INCREASED_FUEL = 0.9

    def refuel(self, fuel):
        super().refuel(fuel)


class Truck(Vehicle):
    _INCREASED_FUEL = 1.6

    def refuel(self, fuel):
        super().refuel(fuel * 0.95)



