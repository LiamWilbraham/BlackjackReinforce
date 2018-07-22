import numpy as np

class Player:
    def __init__(self, name, auto):
        
        '''Creates a Blackjack Player (also used for the dealer)'''
        
        self.name = name
        self.hand = {}
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
        cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
        return np.sum([cards[i] for i in self.hand]) 
    
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
