from lib.entity.deck import Deck
from lib.entity.player import Player
from lib.entity.game import Game


def main():
    deck = Deck()
    deck.get_new_deck()
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    w = game.play_game()
    print(w)


if __name__ == "__main__":
    main()
