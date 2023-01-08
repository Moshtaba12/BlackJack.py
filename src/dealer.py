import random
from deck import Deck 

# Dealer hand and card dealing rotation
class Dealer():
    def __init__(self, deck):
      self.dealerHand = []
      self.score = 0
      self.deck = deck

    #draw one card from deck after initial deal
    def draw_One(self):
      self.dealerHand.extend(self.deck.draw(1))
      self.checkScore()
      if self.score > 21:
        return 1
      return 0
    
    #Deal intial card from the deck and check for score
    def deal_Card(self):
      self.dealerHand.extend(self.deck.draw(2))
      self.checkScore()
      if self.score > 21:
        return 1
      return 0 

    #Check score and increment Ace counter for dealer
    def checkScore(self):
      ace_counter = 0
      self.score = 0
      for card in self.dealerHand:
        if card.price() == 11:
          ace_counter += 1
        self.score += card.price()
      
      #while loop for Multiple Ace draws and Score > 21
      while ace_counter != 0 and self.score > 21:
        ace_counter -= 1
        self.score -= 10
      return self.score
    
    #for loop dealerHand array calling show method (from card)
    def dealer_Show(self):
      print("Dealers hand")
      for i in self.dealerHand:
        i.show()
      print("Dealers score: ", self.score)
