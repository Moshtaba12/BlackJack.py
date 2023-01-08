import unittest
import sys
sys.path.append("c:/Users/Moshtaba/Documents/Coding projects/BBC/segs-2022-tech-test-candidate-pack/segs_blackjack_starter/src")

from src.deck import Deck
class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.deck.create_Deck()

    def tearDown(self):  # this method will be run after each tests
        pass
    
    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)



if __name__ == '__main__':
    unittest.main()
