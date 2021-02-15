import player
from display import Dialogues

valid_bids = [15, 20, 25, 30]

def flip(players, player_list, kitty, deck):
    display = Dialogues()
    # flip = input("Flip card for suit(Y), or bid(n)? [Y/N]")
    flip = display.flipDiag(1)
    if flip.upper() == "y".upper():
        flip = player.Player("flipcard")
        flip.draw(deck, 1)
        # print("Flipped Card, the following game follows this SUIT, this card can't be used:")
        display.flipDiag(2)
        flip.showHand()
        highest_bid, bidder_info = bidding(player_list, flip)
    else:
        highest_bid, bidder_info = bidding(player_list)
        players[bidder_info[0]].bid = highest_bid
        players[bidder_info[0]].takeKitty(kitty)
    deck.onSuit = bidder_info[1]
    player_order = shufflePlayers(player_list, bidder_info)
    # print(f"{bidder_info[0]} Highest Bidder's hand:")
    display.flipDiag(3, {bidder_info[0]})

    players[bidder_info[0]].showHand()
    return players, deck, player_order


def bidding(player_list, flip=False):
    display = Dialogues()
    global valid_bids
    bids_taken = {}
    bid = 0
    bd = 0
    game_suit = ""
    last = ""
    for p in player_list:
        set_bid = False
        if p is player_list[0]:
            valid_bids, game_suit, bid = askBid(p, player_list, flip)
            set_bid = True
        elif len(valid_bids) > 0:
            valid_bids, game_suit, bid = askBid(p, player_list, flip)
            set_bid = True
        if set_bid:
            bids_taken[bid] = [p, game_suit]

        for b in bids_taken:
            if b.isdigit():
                # print("bd", bd)
                display.bidDiag(valid_bids, player, player_list, 8, bd)
                if int(b) > bd:
                    bd = int(b)
        if bd == 0:
            # print(f"Player {p} passed.")
            display.bidDiag(valid_bids, player, player_list, 5, p)

        else:
            if last != f"Highest bid thus far: {bd} {bids_taken[str(bd)]}":
                # print(f"Highest bid thus far: {bd} {bids_taken[str(bd)]}")
                display.bidDiag(valid_bids, player, player_list, 6, f"{bd}, {bids_taken[str(bd)]}")
            last = f"Highest bid thus far: {bd} {bids_taken[str(bd)]}"
    # print("Bidding is over.")
    display.bidDiag(valid_bids, player, player_list, 7)
    return bd, bids_taken[str(bd)]


def askBid(player, player_list, flip):
    display = Dialogues()
    global valid_bids
    # passable = ", or (P)ASS"
    game_suit = ""
    # if len(valid_bids) == 4 and player == player_list[-1]:
        # passable = ""
    # bid = input(f"Now, how much to bid? {valid_bids}{passable}>")
    bid = display.bidDiag(valid_bids, player, player_list, 1)
    if bid.upper() != 'p'.upper() and bid.upper() != 'pass'.upper():
        valid_bids = [v for v in valid_bids if v > int(bid)]
        if not flip:
            # print("OK, Select the suit you want to bid on")
            # suit = input("Select Suit: 1 Hearts, 2 Diamonds, 3 Spades, 4 Clubs>")
            suit = display.bidDiag(valid_bids, player, player_list, 2)
            if int(suit) == 1:
                game_suit = "Hearts"
            elif int(suit) == 2:
                game_suit = "Diamonds"
            elif int(suit) == 3:
                game_suit = "Spades"
            elif int(suit) == 4:
                game_suit = "Clubs"
            # print(f"You chose {game_suit}")
            display.bidDiag(valid_bids, player, player_list, 3, game_suit)
        else:
            game_suit = flip.hand[0].suit
            # print(game_suit)
            # print(f"Suit {game_suit} forced by Card Flip!")
            display.bidDiag(valid_bids, player, player_list, 4, game_suit)


    return valid_bids, game_suit, bid


def shufflePlayers(player_list, bidder_info):
    display = Dialogues()
    player_order = []
    ord = 0
    # print("Bidding is over, highest bidder starts first.")
    # print("Original Order...")
    display.shuffDiag(1)
    for p in player_list:
        # print(p)
        display.shuffDiag(3, p)
    for p in player_list:
        if bidder_info[0] == p:
            player_order.append(p)
        ord += 1
    for e, p in enumerate(player_list):
        if p not in player_order:
            if e > ord:
                player_order.append(p)
    for p in player_list:
        if p not in player_order:
            player_order.append(p)
    # print("Reshuffled order...")
    display.shuffDiag(2)
    for p in player_order:
        # print(p)
        display.shuffDiag(3, p)
    return player_order

def dumpCards(player_order, deck, players):
    display = Dialogues()
    for p in player_order:
        done = False
        while not done and len(players[p].hand) > 1:
            # print(f"Game Suit: {deck.onSuit}")
            # print(f"Player {p}, please discard, you MUST keep 1.")
            display.dumpCardDiag(1, deck.onSuit)
            display.dumpCardDiag(2, p)
            for e, c in enumerate(players[p].hand):
                # print(e, c.face, c.suit)
                display.dumpCardDiag(7, f"{e} {c.face}, {c.suit}")
            # rem = input("Select Card# to remove, ENTER to cancel>")
            rem = display.dumpCardDiag(3)
            if len(rem) > 0:
                for e, c in enumerate(players[p].hand):
                    if int(rem) == e:
                        players[p].hand.remove(c)
                # choice = input("Done? Y/N")
                # if choice.upper() == "Y".upper() or choice.upper() == "Yes".upper():
                #    done = True
                done = display.dumpCardDiag(4)
            else:
                done = display.dumpCardDiag(4)
        # print("You're done discarding...")
    # print("Now you'll all get new cards, up to 5 in your hand...")
    display.dumpCardDiag(5)
    for p in player_order:
        players[p].draw(deck, 5-len(players[p].hand))
        # print(f"{players[p].name}\'s hand")
        display.dumpCardDiag(6, players[p].name)
        players[p].showHand()
    return players, deck
