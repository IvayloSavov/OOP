from typing import List

from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class Hardware:
    name: str
    type: str
    capacity: int
    memory: int
    software_components: List[Software]

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.used_capacity = 0
        self.used_memory = 0
        self.software_components = []
        self.express_software_components = 0
        self.light_software_components = 0

    def install(self, software: Software):
        if (self.used_capacity + software.capacity_consumption > self.capacity) or (
                self.used_memory + software.memory_consumption > self.memory):
            raise Exception("Software cannot be installed")  # TODO: Here should be exception
        if isinstance(software, ExpressSoftware):
            self.express_software_components += 1
        elif isinstance(software, LightSoftware):
            self.light_software_components += 1

        self.used_memory += software.memory_consumption
        self.used_capacity += software.capacity_consumption
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if isinstance(software, ExpressSoftware):
            self.express_software_components -= 1
        elif isinstance(software, LightSoftware):
            self.light_software_components -= 1
        self.used_memory -= software.memory_consumption
        self.used_capacity -= software.capacity_consumption
        self.software_components.remove(software)

    def __str__(self):
        names_of_all_software_components = [sft.name for sft in self.software_components]

        res = (f"Hardware Component - {self.name}\n"
               f"Express Software Components: {self.express_software_components}\n"
               f"Light Software Components: {self.light_software_components}\n"
               f"Memory Usage: {self.used_memory} / {self.memory}\n"
               f"Capacity Usage: {self.used_capacity} / {self.capacity}\n"
               f"Type: {self.type}\n"
               f"Software Components: {', '.join(names_of_all_software_components) if names_of_all_software_components else None}")

        return res.rstrip()
