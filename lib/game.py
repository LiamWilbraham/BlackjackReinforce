from .deck import Deck
from .player import Player

class Game:
    def __init__(self, player_names, verbose):
        
        '''Game class for initialising and playing games'''
        
        self.deck = Deck()
        self.players = [Player(name, auto) for name, auto in player_names.items()]
        self.dealer = Player('Dealer', True)
        self.verbose = verbose
        
    def play(self):
        # deal cards to players and dealer
        
        for player in self.players:
            player.deal(self.deck)
        self.dealer.deal(self.deck)
        
        # play the game
        for player in self.players:
            self.player_turn(player)
        self.dealer_turn()
        
        winners = self.winner
        
        if self.verbose:
            if len(winners) > 0:
                print(*winners, 'won!')
            else:
                print('no winners here!')
        
    def player_turn(self, player):
        # plays a turn for a player
   
        if self.verbose:
            print("\nIt is " + player.name + "'s turn:")
            print('Your hand is: {}. The dealer is showing: {}'.format(player.hand, self.dealer.hand[0]))

        if self.can_split(player.hand):
            self.player_split_or_stick(player)
            if self.verbose:
                player_hands_str = ''
                for hand in player.hands:
                    player_hands_str += str(hand) + ' '
                print('Your hands are: {}. The dealer is showing: {}'.format(player_hands_str, self.dealer.hand[0]))
        
        self.player_hit_or_stick(player)
        
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


    def player_split_or_stick(self, player):
        # see if player wishes to split their hand, if so then do it.
        
        split = False
        if player.auto:
            if player.hand.cards in [['A','A'], ['8','8']]:
                split = True
        else:
            choice = 'invalid'
            while choice.lower() not in ['y', 'n']:
                choice = input('Would you like to split your hand? (y/n) ')
                if choice.lower() == 'y':
                    split = True
                elif choice.lower() != 'n':
                    print("You must answer 'y' or 'n'")
                    
        if split:
            player.split(self.deck)

            
            
    def player_hit_or_stick(self, player):

        for hand in player.hands:
            
            if len(player.hands) > 1 and self.verbose:
                print('Your hand is:', hand)
                
            while (not hand.bust and not hand.blackjack):

                if player.auto:
                    choices = ['h', 's']
                    if hand.score < 17: # player hits when score < 17
                        choice = 'h'
                    else:
                        choice = 's'
                else:
                    choice = input('Would you like to hit or stick? (h/s) ')

                if choice.lower() == 'h':
                    hand.hit(self.deck)
                if self.verbose:
                    print('Your hand is:', hand)
                if choice.lower() == 's':
                    break

                
    def can_split(self, hand):
        # decide if a hand can be split
        if hand.cards[0] == hand.cards[1]:
            return True
        return False

    
    @property
    def winner(self):
        # determine if any players beat the dealer
        
        winners = []
        for player in self.players:
            for hand in player.hands:
                if (hand.score > self.dealer.hand.score and hand.score <= 21) or (self.dealer.hand.score > 21 and hand.score <= 21):
                    winners.append(player.name)
            
        return winners
