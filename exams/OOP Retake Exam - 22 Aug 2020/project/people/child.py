class Child:
    cost: float

    def __init__(self, food_cost: int, *toys_cost):
        self.cost = sum([food_cost, *toys_cost])

    @property
    def month_expenses(self):
        return self.cost * 30
