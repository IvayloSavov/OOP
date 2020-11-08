class Pokemon:
    name: str
    health: int

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{pokemon_name} with health {pokemon_health}"