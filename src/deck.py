import random
from card import Card

#Deck class 
class Deck():
    def __init__(self):
        self.cards = []
   
    #Create deck of 52 cards using Card class
    def create_Deck(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j))
    

    #Draw a random card from generated deck and remove it from the array
    def draw(self,turns):
        cards = []
        for i in range(turns):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    def deck_Count(self):
        #print(len(self.cards))
        return (len(self.cards))
    

# # print tests
# test = Deck()
# test.create_Deck()
# test.deck_Count()
