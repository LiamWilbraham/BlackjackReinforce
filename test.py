from lib import Player, Deck, Game

# simple player test
print('-------------------------------------------------')
print('Player test')
print('-------------------------------------------------')
deck = Deck()
player = Player('Summer')
player.deal(deck)
print(player)
player.hand.hit(deck)
print(player)


# test splitting mechanism
print('-------------------------------------------------')
print('Splitting test')
print('-------------------------------------------------')
game = Game({'Rick' : False, 'Morty' : True}, verbose=True, debug=True)
game.deck.cards = ['10', '10', '8', '8', 'J', '5']  + game.deck.cards
game.play()


# simple game test
print('-------------------------------------------------')
print('Game test:')
print('-------------------------------------------------')
game = Game({'Rick' : False, 'Morty' : True}, verbose=True)
game.play()
