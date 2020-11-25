class Room:
    family_name: str
    budget: float
    members_count: int
    children: list

    def __init__(self, name: str, budget: float, members_count: int):
        self._expenses = 0
        self.room_cost = 0
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []

    @property
    def expenses(self):
        self.calculate_expenses(self.children, self.appliances)
        return self._expenses

    @expenses.setter
    def expenses(self, val):
        if val < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = val

    def calculate_expenses(self, *args):
        total_costs = 0
        for ll in args:
            total_costs += sum(el.month_expenses for el in ll)
        self.expenses = total_costs
        return total_costs

    def __str__(self):
        if self.budget >= self.expenses + self.room_cost:
            self.budget -= self.expenses + self.room_cost
            return f"{self.family_name} paid {self.expenses + self.room_cost:.2f}$ and have {self.budget:.2f}$ left.\n"
        return f"{self.family_name} does not have enough budget and must leave the hotel.\n"

