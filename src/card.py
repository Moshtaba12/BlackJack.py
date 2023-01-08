



class Card:
    def __init__(self,value,suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠'[suit]

    #Print card face and suit
    def show(self):
        print(self.value, self.suit)

    
    #Calculate worth of card
    def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost


#print tests
# test = Card(3,2)
# test.show()
# print(test.price())
