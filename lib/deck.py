import random

class Deck:
    def __init__(self):
        
        '''A simple deck class'''
        
        suit = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11} 
        self.cards = random.sample(list(suit.keys())*4, 52)
    
    def deal(self, n):
        # return the first n cards in the deck
        cards = []
        for i in range(n):
            cards.append(self.cards[0])
            self.cards.pop(0)
        return cards
