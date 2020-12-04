from project.software.software import Software
from math import floor


class LightSoftware(Software):
    type = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        capacity_consumption = floor(capacity_consumption * 150 / 100)
        memory_consumption = floor(memory_consumption * 50 / 100)
        super().__init__(name, self.__class__.type, capacity_consumption, memory_consumption)
