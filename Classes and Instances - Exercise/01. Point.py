import math


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x) -> None:
        self.x = new_x

    def set_y(self, new_y) -> None:
        self.y = new_y

    def distance(self, x, y) -> float:
        a = (self.x - x)**2
        b = (self.y - y)**2
        res = math.sqrt(a + b)
        return res


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
