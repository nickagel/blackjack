from src.lib.entity.player import Player
from src.lib.entity.card import Card


def test_blackjack():
    card1 = Card({"suit": "SPADES", "value": "A"})
    card2 = Card({"suit": "SPADES", "value": "Q"})
    player1 = Player([card1, card2], "nick")
    assert ["SA", "SQ"] == player1.cards
    assert player1.blackjack
    card3 = Card({"suit": "SPADES", "value": "J"})
    card4 = Card({"suit": "SPADES", "value": "Q"})
    player2 = Player([card3, card4], "nick")
    assert player2.blackjack is False
    assert ["SJ", "SQ"] == player2.cards


def test_add_card():
    card1 = Card({"suit": "SPADES", "value": "A"})
    card2 = Card({"suit": "SPADES", "value": "Q"})
    player1 = Player([card1, card2], "nick")
    card3 = Card({"suit": "SPADES", "value": "J"})
    player1.add_card(card3)
    assert ["SA", "SQ", "SJ"] == player1.cards


def test_reached_bust():
    card1 = Card({"suit": "SPADES", "value": "A"})
    card2 = Card({"suit": "SPADES", "value": "Q"})
    card3 = Card({"suit": "SPADES", "value": "Q"})
    player1 = Player([card1, card2], "nick")
    player1.add_card(card3)
    assert player1.reached_bust()
    card4 = Card({"suit": "SPADES", "value": "2"})
    card5 = Card({"suit": "SPADES", "value": "Q"})
    card6 = Card({"suit": "SPADES", "value": "5"})
    player2 = Player([card4, card5], "nick")
    player2.add_card(card6)
    assert player2.reached_bust() is False


def test_reached_limit():
    card1 = Card({"suit": "SPADES", "value": "A"})
    card2 = Card({"suit": "SPADES", "value": "2"})
    card3 = Card({"suit": "SPADES", "value": "Q"})
    player1 = Player([card1, card2], "nick")
    player1.add_card(card3)
    assert player1.reached_limit()
    card4 = Card({"suit": "SPADES", "value": "2"})
    card5 = Card({"suit": "SPADES", "value": "3"})
    card6 = Card({"suit": "SPADES", "value": "5"})
    player2 = Player([card4, card5], "nick")
    player2.add_card(card6)
    assert player2.reached_limit() is False
    card7 = Card({"suit": "SPADES", "value": "10"})
    card8 = Card({"suit": "SPADES", "value": "Q"})
    card9 = Card({"suit": "SPADES", "value": "J"})
    player3 = Player([card7, card8], "nick")
    player3.update_limit(40)
    player3.add_card(card9)
    assert player3.reached_limit() is False
