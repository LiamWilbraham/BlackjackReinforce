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
     
        self.player_hit_or_stick(player)
        
        if self.verbose:
            if player.hand.bust:
                print("{} is bust!".format(player.name))
            elif player.hand.blackjack:
                print("{} has blackjack!".format(player.name)) 
            
    def dealer_turn(self):
        # plays the dealer's turn
        
        if self.verbose:
            print("\nThe dealer's hand is:", self.dealer.hand)
    
        while not self.dealer.hand.bust and self.dealer.hand.score < 17:
            #print('Dealer hits')
            self.dealer.hit(self.deck)
            if self.verbose:
                print("The dealer's hand is:", self.dealer.hand)

    def player_hit_or_stick(self, player):
        
        while (not player.hand.bust and not player.hand.blackjack):
            
            if player.auto:
                choices = ['h', 's']
                if player.hand.score < 17: # player hits when score < 17
                    choice = 'h'
                else:
                    choice = 's'
            else:
                choice = input('Would you like to hit or stick? (h/s)')

            if choice == 'h':
                player.hit(self.deck)
            if self.verbose:
                print('Your hand is:', player.hand)
            if choice == 's':
                break

    @property
    def can_split(hand):
        # decide if a hand can be split
        if hand.card[0] == hand.card[1]:
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
