from typing import List
from movie_world_two.project.customer import Customer
from movie_world_two.project.dvd import DVD


class MovieWorld:
    name: str
    customers: List[Customer]
    dvds: List[DVD]

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def _find_customer(self, customer_id) -> Customer:
        customer = [c for c in self.customers if c.id == customer_id][0]
        return customer

    def add_customer(self, customer) -> None:
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd) -> None:
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self._find_customer(customer_id) # NOTE: Here we may have IndexOutOfRange Exception
        dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id) -> str:
        customer = self._find_customer(customer_id)
        customer_dvds_ids = [dvd.id for dvd in customer.rented_dvds]
        if dvd_id not in customer_dvds_ids:
            return f"{customer.name} does not have that DVD"
        dvd = customer.rented_dvds[customer_dvds_ids.index(dvd_id)]
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        # customer_repr = [repr(c) for c in self.customers]
        # dvds_repr = [repr(d) for d in self.dvds]
        #
        # return "\n".join(customer_repr + dvds_repr)

        return "\n".join(repr(x) for x in (self.customers + self.dvds))


# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)
