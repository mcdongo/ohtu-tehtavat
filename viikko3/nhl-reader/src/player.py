class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return f"{self.name:20}\t{self.team} {str(self.goals):>2} + {str(self.assists):>2} = {str(self.goals+self.assists):>2}"