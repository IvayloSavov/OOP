from abc import ABC, abstractmethod
from project.card.card_repository import CardRepository


class Player(ABC):
    username: str
    health: int
    card_repository: CardRepository
    is_dead: bool

    @abstractmethod
    def __init__(self, username: str, health: int):
        self._username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def is_dead(self):
        if self.health <= 0:
            return True
        return False

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, val):
        if not val:
            raise ValueError("Player's username cannot be an empty string.")
        self._username = val

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self._health = val

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")



