import numpy as np
from .deck import Deck
from .hand import Hand

class Player:
    def __init__(self, name, auto=True):
        
        '''Creates a Blackjack Player (also used for the dealer)'''
        
        self.name = name
        self.hands = []
        self.auto = auto
        self.wallet = 0.0
        
        
    def deal(self, deck):
        # deals cards to the player
        self.hands = [Hand(deck.deal(2))]

        
    def bet(self, amount):
        self.hands[0].bet = amount
        self.wallet -= amount
        
        
    def split(self, deck):
        orig_bet = self.hands[0].bet
        self.hands = [Hand([self.hands[0].cards[0]]), Hand([self.hands[0].cards[1]])]
        self.hands[0].bet = orig_bet
        self.hands[1].bet = orig_bet
        self.wallet -= orig_bet
        self.hands[0].hit(deck)
        self.hands[1].hit(deck)
        

    @property
    def hand(self):
        # return a pointer to the player's first hand (might be the only one)
        return self.hands[0]

    def __str__(self):
        string = "Player " + self.name + ":" + '\n'
        string += "wallet = " + str(self.wallet) + '\n'
        for hand in self.hands:
            string += "hand = " + str(hand.cards) + ', ' 
            string += "score = " + str(hand.score) + ', '
            string += "bet = " + str(hand.bet) + ', '
            string += "blackjack = " + str(hand.blackjack) + ', ' 
            string += "bust = " + str(hand.bust) + '\n'
        return string

