from lib import Player, Deck, Game

# simple player test
deck = Deck()
player = Player('Summer')
player.deal(deck)
print(player)
player.hand.hit(deck)
print(player)


# test splitting mechanism
game = Game({'Rick' : False, 'Morty' : True}, verbose=True)
game.deck.cards = ['10', '10', '8', '8', 'J', '5']  + game.deck.cards
game.play()


# simple game test
game = Game({'Rick' : False, 'Morty' : True}, verbose=True)
game.play()
