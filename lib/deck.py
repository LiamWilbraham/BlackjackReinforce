import random

class Deck:
    def __init__(self):
        
        '''A simple deck class'''
        self.renew()
    
    def deal(self, n):
        # return the first n cards in the deck
        cards = []
        for i in range(n):
            if len(self.cards) == 0:
                self.renew()
            cards.append(self.cards[0])
            self.cards.pop(0)
        return cards

    def renew(self):
        # build a new deck
        suit = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = random.sample(suit*4, 52)
        
