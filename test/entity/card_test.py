from src.lib.entity.card import Card


def test_get_suit_short_name():
    spades_card = Card({"suit": "SPADES", "value": "5"})
    spades_suit_short_name = spades_card.get_suit_short_name()
    assert "S" == spades_suit_short_name
    diamonds_card = Card({"suit": "DIAMONDS", "value": "5"})
    diamonds_suit_short_name = diamonds_card.get_suit_short_name()
    assert "D" == diamonds_suit_short_name
    hearts_card = Card({"suit": "HEARTS", "value": "5"})
    hearts_suit_short_name = hearts_card.get_suit_short_name()
    assert "H" == hearts_suit_short_name
    clubs_card = Card({"suit": "CLUBS", "value": "5"})
    clubs_suit_short_name = clubs_card.get_suit_short_name()
    assert "C" == clubs_suit_short_name


def test_get_card_value():
    numeric_card = Card({"suit": "SPADES", "value": "5"})
    numeric_value = numeric_card.get_card_value()
    assert 5 == numeric_value
    king_card = Card({"suit": "SPADES", "value": "K"})
    king_value = king_card.get_card_value()
    assert 10 == king_value
    queen_card = Card({"suit": "SPADES", "value": "Q"})
    queen_value = queen_card.get_card_value()
    assert 10 == queen_value
    jack_card = Card({"suit": "SPADES", "value": "J"})
    jack_value = jack_card.get_card_value()
    assert 10 == jack_value


def test_get_formatted_card():
    numeric_card = Card({"suit": "SPADES", "value": "5"})
    numeric_formatted_card = numeric_card.get_formatted_card()
    assert "S5" == numeric_formatted_card
    king_card = Card({"suit": "CLUBS", "value": "K"})
    king_formatted_card = king_card.get_formatted_card()
    assert "CK" == king_formatted_card
    queen_card = Card({"suit": "DIAMONDS", "value": "Q"})
    queen_formatted_card = queen_card.get_formatted_card()
    assert "DQ" == queen_formatted_card
    jack_card = Card({"suit": "HEARTS", "value": "J"})
    jack_formatted_card = jack_card.get_formatted_card()
    assert "HJ" == jack_formatted_card
