import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame()
        self.card_1 = Card("Hearts", 1)
        self.card_2 = Card("Spades", 7)
        self.card_3 = Card("Diamonds", 7)

    def test_check_for_ace__returns_True():
        card_is_ace = self.cardgame.check_for_ace(self.card_1)
        self.assertTrue(card_is_ace)

    def test_check_for_ace__returns_False():
        card_is_ace = self.cardgame.check_for_ace(self.card_2)
        self.assertFalse(card_is_ace)

    def test_highest_card__returns_card():
        highest_card = self.cardgame.highest_card(card_1, card_2)
        self.assertEqual(card_2, highest_card)

    def test_highest_card__returns_None():
        highest_card = self.cardgame.highest_card(card_2, card_3)
        self.assertEqual(None, highest_card)

    def test_cards_total__returns_zero():
        self.cards = []
        total = self.cardgame.cards_total(self.cards)
        self.assertEqual(0, total)

    def test_cards_total__returns_total():
        self.cards = [self.card_1, self.card_2, self.card_3]
        total = self.cardgame.cards_total(self.cards)
        self.assertEqual(15, total)