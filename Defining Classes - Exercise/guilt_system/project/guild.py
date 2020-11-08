from guilt_system.project.player import Player
from typing import List


class Guild:
    name: str
    players: List[Player]

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guilt != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guilt = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player_names = [p.name for p in self.players]
        if player_name not in player_names:
            return f"Player {player_name} is not in the guild."
        del self.players[player_names.index(player_name)]
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        res = f"Guild: {self.name}\n"
        players_info = [p.player_info() for p in self.players]
        res += "".join(players_info)
        return res


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
