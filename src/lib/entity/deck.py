from .card import Card
from lib.utils.api_request import ApiRequest


class Deck:
    def __init__(self):
        self.deck_url = "https://pickatale-backend-case.herokuapp.com/shuffle"
        self.deck = []

    def get_new_card(self):
        return Card(self.deck.pop())

    def get_new_deck(self):
        self.deck = ApiRequest.get_json(url=self.deck_url)
