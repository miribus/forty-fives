import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.face = val
        self.trump = False
        self.onsuitVal = 0
        self.offsuitVal = 0

    def show(self):
        print("{} of {}".format(self.face, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.onSuit = ""

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(2, 15):
                if v == 11:
                    v = "Jack"
                elif v == 12:
                    v = "Queen"
                elif v == 13:
                    v = "King"
                elif v == 14:
                    v = "Ace"
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self, number):
        for n in range(1, number+1):
            for i in range(len(self.cards) - 1, 0, -1):
                r = random.randint(0, i)
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            print(f"Shuffle {n}")


    def drawCard(self):
        return self.cards.pop()

