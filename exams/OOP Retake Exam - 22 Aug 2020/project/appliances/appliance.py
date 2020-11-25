class Appliance:
    cost: float

    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * 30

    @property
    def month_expenses(self):
        return self.get_monthly_expense()