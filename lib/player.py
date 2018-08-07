import numpy as np
from .deck import Deck
from .hand import Hand

class Player:
    def __init__(self, name, auto=True):
        
        '''Creates a Blackjack Player (also used for the dealer)'''
        
        self.name = name
        self.hands = [[]]
        self.auto = auto
        self.i = 0 # the current hand index
        
        
    def deal(self, deck):
        # deals cards to the player
        self.hands[self.i] = Hand(deck.deal(2))
 
    def hit(self, deck):
        # deals one additional card to the player
        self.hand.add_card(deck.deal(1)[0])
    
    def stick(self):
        pass

    def split(self):
        pass

    @property
    def hand(self):
        # returns a pointer to the current hand
        return self.hands[self.i] 


    def __str__(self):
        string = "Player " + self.name + ":" + '\n'
        for hand in self.hands:
            string += "hand =" + str(hand.cards) + '\n' 
            string += "score = " + str(hand.score) + '\n' 
            string += "blackjack = " + str(hand.blackjack) + '\n' 
            string += "bust = " + str(hand.bust) + '\n'
        return string

