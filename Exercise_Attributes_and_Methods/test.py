class Customer:
    customers_count = 0

    def __init__(self, name: str, address: str, email: str):
        Customer.customers_count += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.customers_count

ashley = Customer("Ash", "hello", "hello")
ivo = Customer("ivo", "hello", "hello")
bogi = Customer("bogi", "hello", "hello")
ivo = Customer("ivo", "hello", "hello")


print(ashley.id)
print(ivo.id)
print(bogi.id)