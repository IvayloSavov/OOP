from abc import ABC


class Player(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Beginner(Player):
    def __init__(self, username, health=50):
        super().__init__(username, health)


beginner = Beginner("Ivo")
print(beginner.health)