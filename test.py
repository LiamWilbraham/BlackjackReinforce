from lib import Player, Deck, Game

# simple player test
deck = Deck()
player = Player('Alice')
player.deal(deck)
print(player)
player.hit(deck)
print(player)

# simple game test
game = Game({'Alice' : False, 'Bob' : True}, verbose=True)
game.play()

    
