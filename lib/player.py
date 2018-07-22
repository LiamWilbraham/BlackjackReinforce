import numpy as np
from .deck import Deck

class Player:
    def __init__(self, name, auto=True):
        
        '''Creates a Blackjack Player (also used for the dealer)'''
        
        self.name = name
        self.hand = []
        self.auto = auto
            
    def deal(self, deck):
        # deals cards to the player
        self.hand = deck.deal(2)
 
    def hit(self, deck):
        # deals one additional card to the player
        self.hand.append(deck.deal(1)[0])
    
    def stick(self):
        pass

    @property
    def score(self):
        # player score
        face_cards = ['J', 'Q', 'K']
        score = 0
        n_aces = 0

        # initial parse
        for card in self.hand:
            if card == 'A':
                n_aces += 1
            elif card in face_cards:
                score += 10
            else:
                score += int(card)
                
        # handle the aces
        for i in range(n_aces):
            if score <= 10:
                score += 11
            else:
                score += 1
                
        return score
                
    @property
    def bust(self):
        # player is bust
        if self.score > 21:
            return True
        return False
    
    @property
    def blackjack(self):
        # player has blackjack
        if self.score == 21:
            return True
        return False

    def __str__(self):
        string = "Player " + self.name + ":" + '\n'
        string += "hand =" + str(self.hand) + '\n' 
        string += "score = " + str(self.score) + '\n' 
        string += "blackjack = " + str(self.blackjack) + '\n' 
        string += "bust = " + str(self.bust) + '\n'
        return string

