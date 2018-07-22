import random

class Deck:
    def __init__(self):
        
        '''A simple deck class'''
        
        suit = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = random.sample(suit*4, 52)
    
    def deal(self, n):
        # return the first n cards in the deck
        cards = []
        for i in range(n):
            cards.append(self.cards[0])
            self.cards.pop(0)
        return cards
