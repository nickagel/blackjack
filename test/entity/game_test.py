from src.lib.entity.player import Player
from src.lib.entity.deck import Deck
from src.lib.entity.game import Game


def test_bob_win():
    shuffled_deck = [
        {"suit": "SPADES", "value": "A"},
        {"suit": "SPADES", "value": "2"},
        {"suit": "CLUBS", "value": "6"},
        {"suit": "CLUBS", "value": "A"},
        {"suit": "DIAMONDS", "value": "2"},
        {"suit": "DIAMONDS", "value": "J"},
        {"suit": "CLUBS", "value": "8"},
        {"suit": "SPADES", "value": "K"},
        {"suit": "DIAMONDS", "value": "7"},
    ]
    deck = Deck()
    deck.deck = shuffled_deck
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    results = game.play_game()
    assert {
        "winner": "Bob",
        "players": [
            {"name": "player1", "points": 17, "cards": ["D7", "SK"]},
            {"name": "Bob", "points": 18, "cards": ["C8", "DJ"]},
        ],
    } == results


def test_player1_win():
    shuffled_deck = [
        {"suit": "SPADES", "value": "A"},
        {"suit": "SPADES", "value": "2"},
        {"suit": "CLUBS", "value": "6"},
        {"suit": "CLUBS", "value": "A"},
        {"suit": "DIAMONDS", "value": "2"},
        {"suit": "SPADES", "value": "K"},
        {"suit": "DIAMONDS", "value": "7"},
        {"suit": "DIAMONDS", "value": "J"},
        {"suit": "CLUBS", "value": "8"},
    ]
    deck = Deck()
    deck.deck = shuffled_deck
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    results = game.play_game()
    print(results)
    assert {
        "winner": "Bob",
        "players": [
            {"name": "player1", "points": 18, "cards": ["C8", "DJ"]},
            {"name": "Bob", "points": 19, "cards": ["D7", "SK", "D2"]},
        ],
    } == results


def test_bob_bust():
    shuffled_deck = [
        {"suit": "SPADES", "value": "A"},
        {"suit": "SPADES", "value": "2"},
        {"suit": "CLUBS", "value": "6"},
        {"suit": "CLUBS", "value": "A"},
        {"suit": "DIAMONDS", "value": "2"},
        {"suit": "DIAMONDS", "value": "J"},
        {"suit": "CLUBS", "value": "8"},
        {"suit": "SPADES", "value": "K"},
    ]
    deck = Deck()
    deck.deck = shuffled_deck
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    results = game.play_game()
    assert {
        "winner": "player1",
        "players": [
            {"name": "player1", "points": 18, "cards": ["SK", "C8"]},
            {"name": "Bob", "points": 23, "cards": ["DJ", "D2", "CA"]},
        ],
    } == results


def test_player1_bust():
    shuffled_deck = [
        {"suit": "SPADES", "value": "A"},
        {"suit": "SPADES", "value": "2"},
        {"suit": "CLUBS", "value": "6"},
        {"suit": "CLUBS", "value": "A"},
        {"suit": "DIAMONDS", "value": "2"},
        {"suit": "DIAMONDS", "value": "J"},
    ]
    deck = Deck()
    deck.deck = shuffled_deck
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    results = game.play_game()
    assert {
        "winner": "Bob",
        "players": [
            {"name": "player1", "points": 25, "cards": ["DJ", "D2", "S2", "SA"]},
            {"name": "Bob", "points": 17, "cards": ["CA", "C6"]},
        ],
    } == results


def test_player1_blackjack():
    shuffled_deck = [
        {"suit": "SPADES", "value": "A"},
        {"suit": "SPADES", "value": "2"},
        {"suit": "CLUBS", "value": "6"},
        {"suit": "CLUBS", "value": "A"},
        {"suit": "DIAMONDS", "value": "A"},
        {"suit": "DIAMONDS", "value": "J"},
    ]
    deck = Deck()
    deck.deck = shuffled_deck
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    results = game.play_game()
    assert {
        "winner": "player1",
        "players": [
            {"name": "player1", "points": 21, "cards": ["DJ", "DA"]},
            {"name": "Bob", "points": 17, "cards": ["CA", "C6"]},
        ],
    } == results


def test_bob_blackjack():
    shuffled_deck = [
        {"suit": "SPADES", "value": "A"},
        {"suit": "SPADES", "value": "2"},
        {"suit": "DIAMONDS", "value": "A"},
        {"suit": "DIAMONDS", "value": "J"},
        {"suit": "CLUBS", "value": "6"},
        {"suit": "CLUBS", "value": "A"},
    ]
    deck = Deck()
    deck.deck = shuffled_deck
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    results = game.play_game()
    print(results)
    assert {
        "winner": "Bob",
        "players": [
            {"name": "player1", "points": 17, "cards": ["CA", "C6"]},
            {"name": "Bob", "points": 21, "cards": ["DJ", "DA"]},
        ],
    } == results


def test_both_blackjack():
    shuffled_deck = [
        {"suit": "SPADES", "value": "2"},
        {"suit": "SPADES", "value": "A"},
        {"suit": "SPADES", "value": "J"},
        {"suit": "DIAMONDS", "value": "A"},
        {"suit": "DIAMONDS", "value": "J"},
    ]
    deck = Deck()
    deck.deck = shuffled_deck
    player1 = Player(name="player1", hand=[deck.get_new_card(), deck.get_new_card()])
    bob = Player(name="Bob", hand=[deck.get_new_card(), deck.get_new_card()])
    game = Game(deck, player1, bob)
    results = game.play_game()
    print(results)
    assert {
        "winner": None,
        "players": [
            {"name": "player1", "points": 21, "cards": ["DJ", "DA"]},
            {"name": "Bob", "points": 21, "cards": ["SJ", "SA"]},
        ],
    } == results
