class Customer:
    name: str
    address: str
    email: str
    _customers_count = 0

    def __init__(self, name: str, address: str, email: str):
        Customer._customers_count += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer._customers_count

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @classmethod
    def get_next_id(cls) -> int:
        return cls._customers_count + 1
