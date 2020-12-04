from project.software.software import Software
from math import floor


class ExpressSoftware(Software):
    type = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        memory_consumption = memory_consumption * 2
        super().__init__(name, self.__class__.type, capacity_consumption, memory_consumption)
