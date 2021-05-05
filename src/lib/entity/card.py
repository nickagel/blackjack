class Card:
    def __init__(self, card):
        self.suit = card["suit"]
        self.value = card["value"]

    @property
    def CLUBS(self):
        return "C"

    @property
    def DIAMONDS(self):
        return "D"

    @property
    def HEARTS(self):
        return "H"

    @property
    def SPADES(self):
        return "S"

    def get_suit_short_name(self):
        return eval(f"self.{self.suit}")

    def get_card_value(self):
        if self.value in ["K", "Q", "J"]:
            return 10
        elif self.value == "A":
            return 11
        else:
            return int(self.value)

    def get_formatted_card(self):
        return f"{self.get_suit_short_name()}{self.value}"
