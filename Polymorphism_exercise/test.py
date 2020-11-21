class Demo:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val


ivo = Demo("Ivo")
ivo.name = "Ivaylo"
print(ivo.name)
