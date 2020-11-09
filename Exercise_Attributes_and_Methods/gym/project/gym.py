class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer) -> None:
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer) -> None:
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment) -> None:
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan) -> None:
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription) -> None:
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        res = [repr(x) for x in (self.subscriptions + self.customers + self.trainers + self.equipment + self.plans)
               if x.id == subscription_id]
        return "\n".join(res)