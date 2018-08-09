import numpy as np
from .deck import Deck
from .hand import Hand

class Player:
    def __init__(self, name, auto=True):
        
        '''Creates a Blackjack Player (also used for the dealer)'''
        
        self.name = name
        self.hands = []
        self.auto = auto
        
        
    def deal(self, deck):
        # deals cards to the player
        self.hands = [Hand(deck.deal(2))]

        
    def split(self, deck):
        self.hands = [Hand([self.hands[0].cards[0]]), Hand([self.hands[0].cards[1]])]
        self.hands[0].hit(deck)
        self.hands[1].hit(deck)
        

    @property
    def hand(self):
        # return a pointer to the player's first hand (might be the only one)
        return self.hands[0]

    def __str__(self):
        string = "Player " + self.name + ":" + '\n'
        for hand in self.hands:
            string += "hand =" + str(hand.cards) + '\n' 
            string += "score = " + str(hand.score) + '\n' 
            string += "blackjack = " + str(hand.blackjack) + '\n' 
            string += "bust = " + str(hand.bust) + '\n'
        return string

