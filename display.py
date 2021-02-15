# start game


class Dialogues:
    def showCard(self, d):
        print(d)

    def flipDiag(self, c, d=""):
        if c == 1:
            flip = input("Flip card for suit(Y), or bid(n)? [Y/N]")
            return flip
        elif c == 2:
            print("Flipped Card, the following game follows this SUIT, this card can't be used:")
        elif c == 3:
            print(f"{d} Highest Bidder's hand:")

    def bidDiag(self, valid_bids, player, player_list, c, d="", dd=""):
        if c == 1:
            passable = ", or (P)ASS"
            if len(valid_bids) == 4 and player == player_list[-1]:
                passable = ""
            bid = input(f"Now, how much to bid? {valid_bids}{passable}>")
            return bid
        elif c == 2:
            print("OK, Select the suit you want to bid on")
            suit = input("Select Suit: 1 Hearts, 2 Diamonds, 3 Spades, 4 Clubs>")
            return suit
        elif c == 3:
            print(f"You chose {d}")
        elif c == 4:
            print(d)
            print(f"Suit {d} forced by Card Flip!")
        elif c == 5:
            print(f"Player {d} passed.")
        elif c == 6:
            print(f"Highest bid thus far: {d} {dd}")
        elif c == 7:
            print("Bidding is over.")
        elif c == 8:
            print("bd", d)

    def shuffDiag(self, c, d=""):
        if c == 1:
            print("Bidding is over, highest bidder starts first.")
            print("Original Order...")
        elif c == 2:
            print("Reshuffled order...")
        elif c == 3:
            print(d)
        elif c == 4:
            print(f"Shuffle {d}")

    def dumpCardDiag(self, c, d=""):
        if c == 1:
            print(f"Game Suit: {d}")
        elif c == 2:
            print(f"Player {d}, please discard, you MUST keep 1.")
        elif c == 3:
            rem = input("Select Card# to remove, ENTER to cancel>")
            return rem
        elif c == 4:
            choice = input("Done? Y/N")
            if choice.upper() == "Y".upper() or choice.upper() == "Yes".upper():
                return True
            else:
                return False
        elif c == 5:
            print("You're done discarding...")
            print("Now you'll all get new cards, up to 5 in your hand...")
        elif c == 6:
            print(f"{d}\'s hand")
        elif c == 7:
            print(d)
