from collections import defaultdict


class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = defaultdict(int)

    @classmethod
    def from_size(cls, name, type, size):
        capacity: int = size // 2
        return Store(name, type, capacity)

    def add_item(self, item_name):
        products_count = sum(self.items.values())
        if self.capacity > products_count:
            self.items[item_name] += 1
            return f"{item_name} added to the store"
        return "Not enough capacity in the store"

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"