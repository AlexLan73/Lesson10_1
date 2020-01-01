import unittest
import pytest
import OneGames as og
import copy

class Test_test_1(unittest.TestCase):
    def test_1_count_cart(self):
        self.deck = og.Deck()
        self.assertEqual(self.deck.count_card,36)

    def test_2_mix_deck(self):
        self.deck = og.Deck()
        self.lsdeck0 = copy.deepcopy(list(self.deck.deck.keys()))
        self.ls = self.deck.mix_deck()
        self.assertNotEqual(self.lsdeck0, self.ls)

    def test_3_read_card(self):
        self.deck = og.Deck()
        self.deck.mix_deck()
        self.dd = self.deck.read_carf(3)
        self.assertEqual(len(self.dd), 3)

    def test_4_read_card(self):
        self.deck = og.Deck()
        self.deck.mix_deck()
        self.dd1 = self.deck.read_carf(3)
        self.dd2 = self.deck.read_carf(3)
        self.assertNotEqual(list(self.dd1.keys()), list(self.dd2.keys()))

    def test_5_one_card(self):
        self.deck = og.Deck()
        self.deck.mix_deck()
        self.dd1 = list(self.deck.read_carf(1))
        self.assertTrue(self.dd1[0] > 0)


if __name__ == '__main__':
    unittest.main()
#    Test_test_1.test_1_count_cart()