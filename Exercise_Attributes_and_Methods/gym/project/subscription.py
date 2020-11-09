class Subscription:
    _count_subscriptions = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        Subscription._count_subscriptions += 1
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription._count_subscriptions

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @classmethod
    def get_next_id(cls):
        return cls._count_subscriptions + 1
