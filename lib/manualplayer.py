from .baseplayer import BasePlayer

class ManualPlayer(BasePlayer):

        def __init__(self, name, verbose):
            super(ManualPlayer, self).__init__(name, verbose)


        def place_bet(self):
            # place a player bet on the dealt hand

            while True:
                try:
                    bet = float(input('How much would you like to bet? '))
                except ValueError:
                    print('Invalid input')
                    continue
                if self.verbose:
                    print()
                break
            self._bet(bet)


        def split_or_stick(self, deck):
            # see if player wishes to split their hand, if so then do it.

            split = False
            choice = 'invalid'
            while choice.lower() not in ['y', 'n']:
                choice = input('Would you like to split your hand? (y/n) ')
                if choice.lower() == 'y':
                    split = True
                elif choice.lower() != 'n':
                    print("You must answer 'y' or 'n'")

            if split:
                self._split(deck)


        def hit_or_stick(self, deck):

            for hand in self.hands:

                if len(self.hands) > 1 and self.verbose:
                    print('Your hand is:', hand)

                while (not hand.bust and not hand.blackjack):
                    choice = input('Would you like to hit or stick? (h/s) ')

                    if choice.lower() == 'h':
                        hand.hit(deck)
                    if self.verbose:
                        print('Your hand is:', hand)
                    if choice.lower() == 's':
                        break
