from project import *


class Mouse(Mammal):
    _PREFERRED_FOOD = tuple([Vegetable, Fruit])
    _INCREASE_WEIGHT = 0.10

    def make_sound(self):
        return "Squeak"


class Cat(Mammal):
    _PREFERRED_FOOD = tuple([Vegetable, Meat])
    _INCREASE_WEIGHT = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    _PREFERRED_FOOD = tuple([Meat])
    _INCREASE_WEIGHT = 1.00

    def make_sound(self):
        return "ROAR!!!"


class Dog(Mammal):
    _PREFERRED_FOOD = tuple([Meat])
    _INCREASE_WEIGHT = 0.40

    def make_sound(self):
        return "Woof!"

