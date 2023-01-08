


#Players hand 
class Player():
    def __init__(self, deck):
      self.playerHand = []
      self.score = 0
      self.deck = deck
    
    #function for asking for a card
    def hit(self):
      self.playerHand.extend(self.deck.draw(1))
      self.check_Score()
      if self.score > 21:
        return 1
      return 0 

    #From the deck parameter passed, draw method is called to take 2 cards out and extend it to the player hand
    def deal_Card(self):
      self.playerHand.extend(self.deck.draw(2))
      self.check_Score()
      if self.score > 21:
        return 1
      return 0 
      
    #Check score and increment Ace counter for player
    def check_Score(self):
      ace_counter = 0
      self.score = 0
      for card in self.playerHand:
        if card.price() == 11:
          ace_counter += 1
        self.score += card.price()
      
      #while loop for Multiple Ace draws and Score > 21
      while ace_counter != 0 and self.score > 21:
        ace_counter -= 1
        self.score -= 10
      return self.score

    def show(self):
      print("Players hand")
      for i in self.playerHand:
        i.show()
      print("Your score: ", self.score)


      

