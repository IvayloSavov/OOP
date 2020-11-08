from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        pass

    def release_pokemon(self, pokemon_name: str) -> str:
        pass

    def trainer_data(self):
        pass