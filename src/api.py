from lib.entity.deck import Deck
from lib.entity.player import Player
from lib.entity.game import Game
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    deck = Deck()
    deck.get_new_deck()
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    return game.play_game()
app.run()