from project.lion import Lion
from project.cheetah import Cheetah
from project.tiger import Tiger
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet
from typing import List, Union


class Zoo:
    name: str
    __budget: int
    __animal_capacity: int
    __workers_capacity: int
    animals: List[Union[Lion, Tiger, Cheetah]]
    workers: List[Union[Keeper, Caretaker, Vet]]

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Union[Lion, Cheetah, Tiger], price: int) -> str:
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if len(self.animals) < self.__animal_capacity:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Union[Vet, Keeper, Caretaker]) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        worker_names = [w.name for w in self.workers]
        if worker_name not in worker_names:
            return f"There is no {worker_name} in the zoo"
        fired_worker = self.workers.pop(worker_names.index(worker_name))
        return f"{fired_worker.name} fired successfully"

    def pay_workers(self) -> str:
        workers_salaries = sum([w.salary for w in self.workers])
        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        animals_expenses = sum([a.get_needs() for a in self.animals])
        if self.__budget >= animals_expenses:
            self.__budget -= animals_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda a: isinstance(a, Lion), self.animals))
        tigers = list(filter(lambda t: isinstance(t, Tiger), self.animals))
        cheetahs = list(filter(lambda ch: isinstance(ch, Cheetah), self.animals))
        res = f"You have {len(self.animals)} animals\n" # if we don't have any type of the animals should we print that we have 0 of them
        res += (f"----- {len(lions)} Lions:\n" + "".join([f"{repr(lion)}\n" for lion in lions])) if lions else ""
        res += (f"----- {len(tigers)} Tigers:\n" + "".join([f"{repr(tiger)}\n" for tiger in tigers])) if tigers else ""
        res += (f"----- {len(cheetahs)} Cheetahs:\n" + "".join([f"{repr(cheetah)}\n" for cheetah in cheetahs])) if cheetahs else ""

        return res.rstrip()

    def workers_status(self):
        keepers = list(filter(lambda k: isinstance(k, Keeper), self.workers))
        caretakers = list(filter(lambda ck: isinstance(ck, Caretaker), self.workers))
        vets = list(filter(lambda v: isinstance(v, Vet), self.workers))
        res = f"You have {len(self.workers)} workers\n" # same note as in animals_status
        res += (f"----- {len(keepers)} Keepers:\n" + "".join([f"{repr(keeper)}\n" for keeper in keepers])) if keepers else ""
        res += (f"----- {len(caretakers)} Caretakers:\n" + "".join([f"{repr(caretaker)}\n" for caretaker in caretakers])) if caretakers else ""
        res += (f"----- {len(vets)} Vets:\n" + "".join([f"{repr(vet)}\n" for vet in vets])) if vets else ""

        return res.rstrip()


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())

