class Laptop:
    def __init__(self, name):
        self.name = name


lenovo = Laptop("lenovo")
lenovo.ram = 16
Laptop.ram = 8
macbook = Laptop("Mc")
print(macbook.ram)