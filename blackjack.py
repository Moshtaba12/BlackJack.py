import sys

#Change path accordingly to access other classes 
sys.path.append("c:/Users/Moshtaba/Documents/Coding projects/BBC/segs-2022-tech-test-candidate-pack/segs_blackjack_starter/src")

from src.deck import Deck
from src.player import Player
from src.dealer import Dealer

class Blackjack():
    def __init__ (self):
        self.deck = Deck()
        self.deck.create_Deck() 

        self.player = Player(self.deck)
        self.dealer = Dealer(self.deck)
    def play(self):
        #Initial hand draw for both dealer and player (2 cards)
        player_draw = self.player.deal_Card()
        dealer_draw = self.dealer.deal_Card()

        #Show both player and dealer hand (future implementation should show just one of the dealers card)
        self.player.show()
        self.dealer.dealer_Show()
        

        if player_draw == 1:
            print("You drew a blackjack")
            if dealer_draw == 1:
                print("Dealer got a blackjack too, its a tie")
                return 1
        
        #input for player to choose whether to hit or draw
        player_Input = ""
        
        #while input != "stand"
        #bust = 0
        #If input == "Hit", draw one card and calculate total through hit method. If > 21 return 1 which = bust
        while player_Input != "S":
            bust = 0
            player_Input = input("[H]it or [S]tand ")

            if player_Input == "H":
                bust = self.player.hit()
                self.player.show()
            if bust == 1:
                print("You busted, Dealer Won")
                return 1    
        self.player.show()
        #If dealer draw = true, they have a blackjack
        if dealer_draw == 1:
            print("Dealer won. They got a blackjack!")
            return 1
        
        #Algorithm for dealer to keep hitting if the score is < 17
        while self.dealer.checkScore() < 17:
            if self.dealer.draw_One() == 1:
                self.dealer.dealer_Show()
                print("Dealer busted. You win!")
                return 1
            self.dealer.dealer_Show()

        #Check if score is = > < dealers 
        if self.dealer.checkScore() == self.player.check_Score():
            print("Its a tie")
        elif self.dealer.checkScore() > self.player.check_Score():
            print("Dealer won, Nice try")
        elif self.dealer.checkScore() < self.player.check_Score():
            print("You won, Congrats!!")




        







game = Blackjack()
game.play()