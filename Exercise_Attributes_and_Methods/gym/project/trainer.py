class Trainer:
    _count_trainers = 0

    def __init__(self, name: str):
        Trainer._count_trainers += 1
        self.name = name
        self.id = Trainer._count_trainers

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @classmethod
    def get_next_id(cls):
        return cls._count_trainers + 1