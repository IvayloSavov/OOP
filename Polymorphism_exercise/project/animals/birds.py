from abc import ABC

from project import Bird, Meat


class Owl(Bird):
    _PREFERRED_FOOD = tuple([Meat])
    _INCREASE_WEIGHT = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    _PREFERRED_FOOD = None
    _INCREASE_WEIGHT = 0.35

    def make_sound(self):
        return "Cluck"
