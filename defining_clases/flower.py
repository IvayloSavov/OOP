class Flower:
    def __init__(self, name, water_requirement):
        self.name = name
        self.water_requirements = water_requirement
        self.is_happy = False

    def water(self, quantity):
        self.is_happy = quantity >= self.water_requirements

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"
