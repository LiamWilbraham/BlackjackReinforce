from .baseplayer import BasePlayer

class AutoPlayer(BasePlayer):

        def __init__(self, name, verbose):
            super(AutoPlayer, self).__init__(name, verbose)


        def player_bet(self):
            # place a player bet on the dealt hand

            bet = 10.0
            if self.verbose:
                print("{}'s hand is {}".format(self.name, self.hand))
                print('{} bets {}'.format(self.name, bet))

            self.bet(bet)


        def player_split_or_stick(self, deck):
            # see if player wishes to split their hand, if so then do it.

            split = False
            if self.hand.cards in [['A','A'], ['8','8']]:
                split = True

            if split:
                self.split(deck)


        def player_hit_or_stick(self, deck):

            for hand in self.hands:

                if len(self.hands) > 1 and self.verbose:
                    print('Your hand is:', hand)

                while (not hand.bust and not hand.blackjack):

                    choices = ['h', 's']
                    if hand.score < 17: # player hits when score < 17
                        choice = 'h'
                    else:
                        choice = 's'

                    if choice.lower() == 'h':
                        hand.hit(deck)
                    if self.verbose:
                        print('Your hand is:', hand)
                    if choice.lower() == 's':
                        break
