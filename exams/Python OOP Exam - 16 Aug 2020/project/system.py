from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from typing import List

from project.software.software import Software


class System:
    _hardware: List[Hardware] = []  # TODO: They could be instance attributes
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in map(lambda hrd: hrd.name, System._hardware):
            return "Hardware does not exist"
        hardware = [hrd for hrd in System._hardware if hrd.name == hardware_name][0]
        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(new_software)
        except Exception as text:
            return str(text)
        else:
            System._software.append(new_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in map(lambda hrd: hrd.name, System._hardware):
            return "Hardware does not exist"
        hardware = [hrd for hrd in System._hardware if hrd.name == hardware_name][0]
        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(new_software)
        except Exception as text:
            return str(text)
        else:
            System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware_names = (hrd.name for hrd in System._hardware)
        software_names = (sft.name for sft in System._software)

        if hardware_name not in hardware_names or software_name not in software_names:
            return "Some of the components do not exist"

        hardware = next(hrd for hrd in System._hardware if hrd.name == hardware_name)
        software = next(sft for sft in System._software if sft.name == software_name)
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        count_of_hardware = len(System._hardware)
        count_of_software = len(System._software)

        total_used_memory = sum(hrd.used_memory for hrd in System._hardware for sft in hrd.software_components)
        total_memory = sum(hrd.memory for hrd in System._hardware)

        total_used_capacity = sum(hrd.used_capacity for hrd in System._hardware)
        total_capacity = sum(hrd.capacity for hrd in System._hardware)

        res = f"System Analysis\n" \
              f"Hardware Components: {count_of_hardware}\n" \
              f"Software Components: {count_of_software}\n" \
              f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
              f"Total Capacity Taken: {total_used_capacity} / {total_capacity}"

        return res

    @staticmethod
    def system_split():
        hrd_info = "".join([str(hrd) for hrd in System._hardware])
        return hrd_info

