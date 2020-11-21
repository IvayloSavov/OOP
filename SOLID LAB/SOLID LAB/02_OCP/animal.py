from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    # def __init__(self, species): # може и без това, тъй като може да върнем вида от името на сътоветния клас
    #     self.species = species

    # def get_species(self):
    #     return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "bau"


class Chicken(Animal):
    def make_sound(self):
        return "chick-chirick"


class Tiger(Animal):
    def make_sound(self):
        return "Roar"


def animal_sound(animals: List[Animal]):  # polymorphic behavior
    for animal in animals:
        print(animal.make_sound())


# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)

animals = [Cat(), Dog(), Chicken(), Tiger()]
animal_sound(animals)

# old
# animals = [Cat('cat'), Dog('dog'), Chicken('chicken'), Tiger('tiger')]
# animal_sound(animals)

# old
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
