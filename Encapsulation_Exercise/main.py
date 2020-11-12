class Number:
    def __init__(self, val):
        self.value = val

    @staticmethod
    def add(a, b):
        return a + b

print(Number.add(2, 3))