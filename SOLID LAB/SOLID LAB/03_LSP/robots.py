from abc import ABC, abstractmethod

# old
# class Robot:
#     def __init__(self, type):
#         self.type = type
#
#     def get_type(self):
#         return self.type
#
#
# class Android(Robot):
#     def android_senzors_count(self):
#         return 4
#
#
# class Chappie(Robot):
#     def chappie_senzors_count(self):
#         return 6
#
#
# def count_robot_senzors(robots: list): # violation: OCP: LCP
#     for robot in robots:
#         if isinstance(robot, Android):
#             print(robot.android_senzors_count())
#         elif isinstance(robot, Chappie):
#             print(robot.chappie_senzors_count())


# new


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    @abstractmethod
    def get_sensors_count(self):
        pass


class Android(Robot):
    def get_sensors_count(self):
        return 4


class Chappie(Robot):
    def get_sensors_count(self):
        return 6


def count_robot_senzors(robots: list): # violation: OCP: LCP
    for robot in robots:
        print(robot.get_sensors_count())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)

robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)
