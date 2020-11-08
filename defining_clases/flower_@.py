from dataclasses import dataclass


class Flower:
    name: str
    water_requirements: int
    is_happy: bool = False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = quantity >= self.water_requirements

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"