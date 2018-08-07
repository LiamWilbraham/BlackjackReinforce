from lib import Player, Deck, Game

# simple player test
deck = Deck()
player = Player('Summer')
player.deal(deck)
print(player)
player.hit(deck)
print(player)

# simple game test
game = Game({'Rick' : False, 'Morty' : True}, verbose=True)
game.play()

    
