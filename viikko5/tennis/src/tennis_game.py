class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if self.player1.get_name() == player_name:
            self.player1.add_point()
            return
        self.player2.add_point()

    def get_score(self):
        scorelist = ["Love","Fifteen","Thirty","Forty"]
        if self.player1.get_score() == self.player2.get_score():
            if self.player1.get_score() not in (0,1,2,3):
                return "Deuce"
            return f"{scorelist[self.player1.get_score()]}-All"
        
        
        if self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
            minus_result = self.player1.get_score() - self.player2.get_score()

            if abs(minus_result) == 1:
                return f"Advantage {self.player1.get_name()}" if minus_result > 0 else f"Advantage {self.player2.get_name()}"
            if abs(minus_result) >= 2:
                return f"Win for {self.player1.get_name()}" if minus_result > 0 else f"Win for {self.player2.get_name()}"
        
        
        return f"{scorelist[self.player1.get_score()]}-{scorelist[self.player2.get_score()]}"

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1
    
    def get_score(self):
        return self.score

    def get_name(self):
        return self.name
    