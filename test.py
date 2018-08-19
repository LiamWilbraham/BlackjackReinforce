from lib import ManualPlayer, AutoPlayer, Deck, Game

# simple player test
print('-------------------------------------------------')
print('Player test')
print('-------------------------------------------------')
deck = Deck()

man_player = ManualPlayer('Summer', True)
man_player.deal(deck)
print(man_player)
man_player.hand.hit(deck)
print(man_player)

auto_player = AutoPlayer('RoboSummer', True)
auto_player.deal(deck)
print(auto_player)
auto_player.hand.hit(deck)
print(auto_player)


# test splitting mechanism
print('-------------------------------------------------')
print('Splitting test')
print('-------------------------------------------------')
game = Game({'Rick' : True, 'Morty' : True}, verbose=True, debug=True)
game = Game({'Rick' : True, 'Morty' : True}, verbose=True, debug=True)
game.deck.cards = ['10', '10', '8', '8', 'J', '5']  + game.deck.cards
game.play()


# simple game test
print('-------------------------------------------------')
print('Game test:')
print('-------------------------------------------------')
game = Game({'Rick' : True, 'Morty' : True}, verbose=True)
game.play()

from lib.strategies import *

dealer_card = '6'
player_card = '12'
print(basic['Hard Total'][dealer_card][player_card])