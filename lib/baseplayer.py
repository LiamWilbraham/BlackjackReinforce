import numpy as np
from .deck import Deck
from .hand import Hand

class BasePlayer:

    def __init__(self, name, verbose):

        '''Creates a Blackjack Player (also used for the dealer)'''

        self.name = name
        self.verbose = verbose
        self.hands = []
        self.wallet = 0.0
        self.n_hands_played = 0
        self.n_hands_won = 0
        self.n_hands_drawn = 0


    def deal(self, deck):
        # deals cards to the player
        self.hands = [Hand(deck.deal(2))]


    def can_split(self, hand):
        # decide if a hand can be split
        if hand.cards[0] == hand.cards[1]:
            return True
        return False


    def collect_winnings(self):
        for hand in self.hands:
            if hand.wins:
                if hand.blackjack:
                    self.wallet += 2.5*hand.bet
                else:
                    self.wallet += 2.0*hand.bet
            elif hand.draws:
                self.wallet += hand.bet


    @property
    def hand(self):
        # return a pointer to the player's first hand (might be the only one)
        return self.hands[0]


    @property
    def win_rate(self):
        if self.n_hands_played > 0:
            return self.n_hands_won*100/self.n_hands_played
        return 0.0
    

    def stats(self):
        # returns the player statistics as a string
        string = "Player " + self.name + " stats:" + '\n'
        string += "hands player = " + str(self.n_hands_played) + '\n'
        string += "hands won = " + str(self.n_hands_won) + '\n'
        string += "hands lost = " + str(self.n_hands_player - self.n_hands_drawn) + '\n'
        string += "hands drawn = " + str(self.n_hands_drawn) + '\n'
        string += "win rate = " + str(self.win_rate) + '%\n'
        return string

    
    # private methods
    def _bet(self, amount):
        self.hands[0].bet = amount
        self.wallet -= amount

        
    def _split(self, deck):
        orig_bet = self.hands[0].bet
        self.hands = [Hand([self.hands[0].cards[0]]), Hand([self.hands[0].cards[1]])]
        self.hands[0].bet = orig_bet
        self.hands[1].bet = orig_bet
        self.wallet -= orig_bet
        self.hands[0].hit(deck)
        self.hands[1].hit(deck)

    # dunder methods
    def __str__(self):
        # return a detailed breakdown of the players hands as a string
        string = "Player " + self.name + ":" + '\n'
        string += "wallet = " + str(self.wallet) + '\n'
        for hand in self.hands:
            string += "hand = " + str(hand.cards) + ', '
            string += "score = " + str(hand.score) + ', '
            string += "bet = " + str(hand.bet) + ', '
            string += "blackjack = " + str(hand.blackjack) + ', '
            string += "bust = " + str(hand.bust) + '\n'
        return string
