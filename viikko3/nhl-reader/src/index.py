import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )

            players.append(player)
    

    print(f"Players from FIN {datetime.now()}")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()