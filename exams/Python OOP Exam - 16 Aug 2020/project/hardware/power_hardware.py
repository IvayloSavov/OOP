from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    type = "Power"

    def __init__(self, name, capacity: int, memory: int):
        super().__init__(name, self.__class__.type, floor(capacity * 25 / 100), floor(memory * 175/100))
