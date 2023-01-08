import unittest
import sys
sys.path.append("c:/Users/Moshtaba/Documents/Coding projects/BBC/segs-2022-tech-test-candidate-pack/segs_blackjack_starter/src")

from src.player import Player
from src.deck import Deck

class PlayerHandTestCase(unittest.TestCase):

  def setUp(self):
    self.deck = Deck()
    self.deck.create_Deck()
    self.player = Player(self.deck)
    self.player.deal_Card()

  def tearDown(self):
    pass

  def test_player_hand_amount(self):
    hand_amount = len(self.player.playerHand)
    self.assertEqual = (hand_amount, 2)