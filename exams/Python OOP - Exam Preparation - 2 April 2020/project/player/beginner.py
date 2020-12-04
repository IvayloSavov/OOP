from project.player.player import Player


class Beginner(Player):

    def __init__(self, username):
        super().__init__(username=username, health=50)

