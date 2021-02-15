import deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bid = 0

    def draw(self, deck, number):
        for i in range(0, number):
            self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def takeKitty(self, kitty):
        for c in kitty.hand:
            self.hand.append(c)



