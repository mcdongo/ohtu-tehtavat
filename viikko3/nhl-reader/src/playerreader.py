import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self, nationality):
        players = []

        for player_dict in self.response:
            if player_dict['nationality'] == nationality:
                player = Player(
                    player_dict['name'],
                    player_dict['team'],
                    player_dict['goals'],
                    player_dict['assists']
                )

                players.append(player)

        return players