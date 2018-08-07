class Hand:
    def __init__(self, cards):
    	self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    @property
    def score(self):
        # player score
        face_cards = ['J', 'Q', 'K']
        score = 0
        n_aces = 0

        # initial parse
        for card in self.cards:
            if card == 'A':
                n_aces += 1
            elif card in face_cards:
                score += 10
            else:
                score += int(card)
                
        # handle the aces
        for i in range(n_aces):
            if score <= 10:
                score += 11
            else:
                score += 1
                
        return score
    
                
    @property
    def bust(self):
        # hand is bust
        if self.score > 21:
            return True
        return False
    
    @property
    def blackjack(self):
        # blackjack hand
        if self.score == 21 and len(this.cards == 2):
            return True
        return False

    
    def __getitem__(self,index):
        # allows Hand to be iterated over 
        return self.cards[index]


    def __str__(self):
        return str(self.cards)
