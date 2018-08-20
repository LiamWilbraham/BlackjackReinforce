from .baseplayer import BasePlayer

class Dealer(BasePlayer):

    def __init__(self, verbose):
        super(Dealer, self).__init__('Dealer', verbose)


    def hit_or_stick(self, deck):
                
        while not self.hand.bust and self.hand.score < 17:
            self.hand.hit(deck)
        if self.verbose:
            print("The dealer's hand is:", self.hand)

