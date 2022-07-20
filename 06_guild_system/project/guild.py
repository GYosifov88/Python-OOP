from project import player
from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for person in self.players:
            result += person.player_info() + '\n'

        return result.strip()