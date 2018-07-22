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

        while (not player.bust and not player.blackjack):
         
            if player.auto:
                choices = ['h', 's']
                #choice = random.choice(choices) # player chooses randomly
                if player.score < 17: # player hits when score < 17
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
        
        if self.verbose:
            if player.bust:
                print("{} is bust!".format(player.name))
            elif player.blackjack:
                print("{} has blackjack!".format(player.name)) 
            
    def dealer_turn(self):
        # plays the dealer's turn
        
        if self.verbose:
            print("\nThe dealer's hand is:", self.dealer.hand)
    
        while not self.dealer.bust and self.dealer.score < 17:
            #print('Dealer hits')
            self.dealer.hit(self.deck)
            if self.verbose:
                print("The dealer's hand is:", self.dealer.hand)

    @property
    def winner(self):
        # determine if any players beat the dealer
        
        winners = []
        for player in self.players:

            if (player.score > self.dealer.score and player.score <= 21) or (self.dealer.score > 21 and player.score <= 21):
                winners.append(player.name)
            
        return winners
