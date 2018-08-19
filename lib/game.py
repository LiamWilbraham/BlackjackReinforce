from .deck import Deck
from .manualplayer import ManualPlayer
from .autoplayer import AutoPlayer

class Game:
    def __init__(self, player_names, verbose, debug=False):

        '''Game class for initialising and playing games'''

        self.deck = Deck()
        self.players = [AutoPlayer(name, verbose) for name, verbose in player_names.items()]
        self.dealer = AutoPlayer('Dealer', False)
        self.verbose = verbose
        self.debug = debug

    def play(self):

        # deal cards to players and dealer
        for player in self.players:
            player.deal(self.deck)
            if self.debug:
                print(player)
        self.dealer.deal(self.deck)
        if self.debug:
            print(self.dealer)

        # place the bets
        for player in self.players:
            if self.verbose:
                print("\nIt is " + player.name + "'s turn:")
                print('Your hand is: {}. The dealer is showing: {}'.format(player.hand, self.dealer.hand[0]))
            player.player_bet()
            if self.debug:
                print(player)

        # play the game
        for player in self.players:
            self.player_turn(player)
        self.dealer_turn()

        # decide who wins, losses and move cash as required
        self.finalise()


    def player_turn(self, player):   ##### should this be moved to manual/auto player too? Not sure.
        # plays a turn for a player

        if self.verbose:
            print("\nIt is " + player.name + "'s turn:")
            print('Your hand is: {}. The dealer is showing: {}'.format(player.hand, self.dealer.hand[0]))

        if self.can_split(player.hand):
            player.player_split_or_stick(self.deck)
            if self.debug:
                print(player)

            if self.verbose:
                player_hands_str = ''
                for hand in player.hands:
                    player_hands_str += str(hand) + ' '
                print('Your hands are: {}. The dealer is showing: {}'.format(player_hands_str, self.dealer.hand[0]))

        player.player_hit_or_stick(self.deck)

        if self.verbose:
            for hand in player.hands:
                if hand.bust:
                    print("{} is bust!".format(player.name))
                elif hand.blackjack:
                    print("{} has blackjack!".format(player.name))


    def dealer_turn(self):
        # plays the dealer's turn

        if self.verbose:
            print("\nThe dealer's hand is:", self.dealer.hand)

        while not self.dealer.hand.bust and self.dealer.hand.score < 17:
            #print('Dealer hits')
            self.dealer.hand.hit(self.deck)
            if self.verbose:
                print("The dealer's hand is:", self.dealer.hand)


    def can_split(self, hand):
        # decide if a hand can be split
        if hand.cards[0] == hand.cards[1]:
            return True
        return False


    def finalise(self):
        # determine if any players beat the dealer and update the relevant player properties

        for player in self.players:
            for i, hand in enumerate(player.hands):
                if hand.bust:
                    # player losses regardless of dealers hand
                    status = 'loss'
                elif not self.dealer.hand.bust and hand.score < self.dealer.hand.score:
                    # delear is not bust, and has a better hand than the player
                    status = 'loss'
                elif self.dealer.hand.bust or hand.score > self.dealer.hand.score:
                    # player wins with a higher hand than dealer, or dealer is bust (but not player)
                    status = 'win'
                elif hand.blackjack and not self.dealer.hand.blackjack:
                    # player has blackjack but not the dealer
                    status = 'win'
                elif hand.blackjack and self.dealer.hand.blackjack:
                    # player and dealer both have blackjack
                    status = 'draw'
                elif hand.score == self.dealer.hand.score:
                    # player and dealer don't have blackjack, but have hands of equal value
                    status = 'draw'

                # update the attributes
                player.n_hands_played += 1
                if status == 'win':
                    player.n_hands_won += 1
                    hand.wins = True
                    if self.verbose:
                        print("{}'s hand {} beats the dealer.".format(str(player.name), str(i)))
                elif status == 'draw':
                    player.n_hands_drawn += 1
                    hand.draws = True
                    if self.verbose:
                        print("{}'s hand {} draws against the dealer.".format(str(player.name), str(i)))
                else:
                    if self.verbose:
                        print("{}'s hand {} looses against the dealer.".format(str(player.name), str(i)))

            # collect any winnngs
            player.collect_winnings()
