class Game:
    def __init__(self, deck, player1, player2):
        self.deck = deck
        self.player1 = player1
        self.player2 = player2

    def determine_winner(self):
        if self.player1.reached_bust():
            return self.player2.name
        elif self.player2.reached_bust():
            return self.player1.name
        elif self.player2.total > self.player1.total:
            return self.player2.name
        elif self.player2.total == self.player1.total:
            return None
        else:
            return self.player1.name

    def game_over(self):
        return {
            "winner": self.determine_winner(),
            "players": [
                {
                    "name": self.player1.name,
                    "points": self.player1.total,
                    "cards": self.player1.cards,
                },
                {
                    "name": self.player2.name,
                    "points": self.player2.total,
                    "cards": self.player2.cards,
                },
            ],
        }

    def play_game(self):
        if self.player1.blackjack or self.player2.blackjack:
            return self.game_over()
        self.player_turn(self.player1)
        if self.player1.reached_bust():
            return self.game_over()
        self.player2.limit = self.player1.total
        self.player_turn(self.player2)
        return self.game_over()

    def player_turn(self, player):
        while not player.reached_limit():
            card = self.deck.get_new_card()
            player.add_card(card)
