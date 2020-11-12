class Customer:
    @property
    def a(self):
        return 42

    @a.setter
    def a(self, value):
        a = value

c = Customer()
c.a = 50
print(c.a)