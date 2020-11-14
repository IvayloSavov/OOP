from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION: float = 8.00

print(type(RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION))