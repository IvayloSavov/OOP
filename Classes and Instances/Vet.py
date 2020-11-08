class Vet:
    animals = []  # Stores all animals in the clinic
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []  # Stores all animals for the current vet

    def register_animal(self, animal_name):
        if len(Vet.animals) < Vet.space:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.pop(self.animals.index(animal_name))
            Vet.animals.pop(Vet.animals.index(animal_name))
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        vet_name = self.name
        amount_of_vet_animals = len(self.animals)
        space_left_in_clinic = Vet.space - len(Vet.animals)
        f"{vet_name} has {amount_of_vet_animals} animals. {space_left_in_clinic} space left in clinic"
