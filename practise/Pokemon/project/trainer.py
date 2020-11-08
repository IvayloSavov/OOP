# from Pokemon.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon.name in pokemon_names:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon_name not in pokemon_names:
            return "Pokemon is not caught"
        pokemon = [p for p in self.pokemon if p.name == pokemon_name][0]
        self.pokemon.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        res = f"Pokemon Trainer {self.name}\n" \
              f"Pokemon count {len(self.pokemon)}\n"
        res += "".join([f"- {p.pokemon_details()}\n" for p in self.pokemon])
        return res


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
