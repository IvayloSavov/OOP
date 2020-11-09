class Equipment:
    _equipment_count = 0

    def __init__(self, name: str):
        Equipment._equipment_count += 1
        self.name = name
        self.id = Equipment._equipment_count

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @classmethod
    def get_next_id(cls) -> int:
        return cls._equipment_count + 1

