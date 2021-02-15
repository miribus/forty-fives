valid_bids = [15, 20, 25, 30]


def bidding(player_list, flip=False):
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
                print("bd", bd)
                if int(b) > bd:
                    bd = int(b)
        if bd == 0:
            print(f"Player {p} passed.")

        else:
            if last != f"Highest bid thus far: {bd} {bids_taken[str(bd)]}":
                print(f"Highest bid thus far: {bd} {bids_taken[str(bd)]}")
            last = f"Highest bid thus far: {bd} {bids_taken[str(bd)]}"
    print("Bidding is over.")
    return bd, bids_taken[str(bd)]


def askBid(player, player_list, flip):
    global valid_bids
    passable = ", or (P)ASS"
    game_suit = ""
    if len(valid_bids) == 4 and player == player_list[-1]:
        passable = ""
    bid = input(f"Now, how much to bid? {valid_bids}{passable}>")
    if bid.upper() != 'p'.upper() and bid.upper() != 'pass'.upper():
        valid_bids = [v for v in valid_bids if v > int(bid)]
        if not flip:
            print("OK, Select the suit you want to bid on")
            suit = input("Select Suit: 1 Hearts, 2 Diamonds, 3 Spades, 4 Clubs>")
            if int(suit) == 1:
                game_suit = "Hearts"
            elif int(suit) == 2:
                game_suit = "Diamonds"
            elif int(suit) == 3:
                game_suit = "Spades"
            elif int(suit) == 4:
                game_suit = "Clubs"
            print(f"You chose {game_suit}")
        else:
            game_suit = flip.hand[0].suit
            print(game_suit)
            print(f"Suit {game_suit} forced by Card Flip!")


    return valid_bids, game_suit, bid


def shufflePlayers(player_list, bidder_info):
    player_order = []
    ord = 0
    print("Bidding is over, highest bidder starts first.")
    print("Original Order...")
    for p in player_list:
        print(p)
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
    print("Reshuffled order...")
    for p in player_order:
        print(p)
    return player_order

def dumpCards(player_order, deck, players):
    for p in player_order:
        remove_cards = []
        done = False
        while not done and len(players[p].hand) > 1:
            print(f"Game Suit: {deck.onSuit}")
            print(f"Player {p}, please discard, you MUST keep 1.")
            for e, c in enumerate(players[p].hand):
                print(e, c.face, c.suit)
            rem = input("Select Card# to remove, ENTER to cancel>")
            if len(rem) > 0:
                for e, c in enumerate(players[p].hand):
                    if int(rem) == e:
                        players[p].hand.remove(c)
                choice = input("Done? Y/N")
                if choice.upper() == "Y".upper() or choice.upper() == "Yes".upper():
                    done = True
        print("You're done discarding...")

    print("Now you'll all get new cards, up to 5 in your hand...")
    for p in player_order:
        players[p].draw(deck, 5-len(players[p].hand))
        print(f"{players[p].name}\'s hand")
        players[p].showHand()
    return players, deck
