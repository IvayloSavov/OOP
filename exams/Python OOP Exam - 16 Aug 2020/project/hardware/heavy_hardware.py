from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):
    type = "Heavy"

    def __init__(self, name, capacity: int, memory: int):
        super().__init__(name, self.__class__.type, capacity * 2, floor(memory * 75/100))
