from typing import List
from project.card.card import Card


class CardRepository:
    count: int
    cards: List[Card]

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        pass

    def remove(self, card: str):
        pass

    def find(self, name: str):
        pass
