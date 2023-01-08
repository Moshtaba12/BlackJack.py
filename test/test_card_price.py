import unittest
import sys
sys.path.append("c:/Users/Moshtaba/Documents/Coding projects/BBC/segs-2022-tech-test-candidate-pack/segs_blackjack_starter/src")

from src.card import Card
from src.deck import Deck
from src.player import Player

class TestCardPrice(unittest.TestCase):

  def setUp(self):
   self.dummy_card = Card(3,2)
   self.king_card = Card(13,2)
   self.ace_card = Card(1,1)
   self.ace_card_two = Card(1,2)
   self.nine_card = Card(9,1)

   self.deck = Deck() 
   self.player_one = Player(self.deck)
   self.player_two = Player(self.deck)

   self.player_one.playerHand = [self.ace_card, self.ace_card_two] #Ace + #Ace
   self.player_two.playerHand = [self.ace_card, self.ace_card_two, self.nine_card]

  def tearDown(self):
    pass

  def test_card_price(self):
    self.price = self.dummy_card.price()
    self.assertEqual(self.price, 3)

  def test_king_and_ace(self):
    self.total = self.king_card.price() + self.ace_card.price()
    self.assertEqual(self.total, 21)

  def test_ace_and_ace(self):
    self.double_ace_total = self.player_one.check_Score()
    self.assertEqual(self.double_ace_total, 12)
    
  def test_nine_ace_king(self):
    self.card_total = self.player_two.check_Score()
    self.assertEqual = (self.card_total, 21)


