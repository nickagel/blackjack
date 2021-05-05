class Player:
    def __init__(self, hand, name):
        self.name = name
        self.cards = []
        self.total = 0
        self.limit = 17
        self.bust = 21
        self.blackjack = False
        self.set_hand(hand)

    def add_card(self, card):
        self.cards.append(card.get_formatted_card())
        self.total += card.get_card_value()

    def reached_bust(self):
        return False if self.bust >= self.total else True

    def reached_limit(self):
        return False if self.limit > self.total else True

    def set_hand(self, hand):
        for card in hand:
            self.add_card(card)
        self.blackjack = True if self.total == self.bust else False

    def update_limit(self, limit):
        self.limit = limit
