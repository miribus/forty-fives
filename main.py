import deck
import player
import play

deck = deck.Deck()
deck.shuffle(7)

#group = input("number of players>")
group = 2
players = {}
player_list = []
#for i in range(0, int(group)):
    #name = input("Player Name>")
    #players[i] = player.Player(name)
    #player_list.append(i)

players["Todd"] = player.Player("Todd")
player_list.append("Todd")
players["Anish"] = player.Player("Anish")
player_list.append("Anish")

kitty = player.Player("Kitty")

# opening deal
print("Opening deal!  3 cards to each player, and the Kitty")
for p in players:
    players[p].draw(deck, 3)
    #print(f"{players[p].name}\'s hand")
    #players[p].showHand()

kitty.draw(deck, 3)
print("Kitty Drawn")
#kitty.showHand()

print("Opening deal!  Now, 2 cards to each player.")
for p in player_list:
    players[p].draw(deck, 2)
    print(f"{players[p].name}\'s hand")
    players[p].showHand()

flip = input("Flip card for suit(Y), or bid(n)? [Y/N]")
if flip.upper() == "y".upper():
    flip = player.Player("flipcard")
    flip.draw(deck, 1)
    print("Flipped Card, the following game follows this SUIT, this card can't be used:")
    flip.showHand()
    highest_bid, bidder_info = play.bidding(player_list, flip)
else:
    highest_bid, bidder_info = play.bidding(player_list)
    players[bidder_info[0]].bid = highest_bid
    players[bidder_info[0]].takeKitty(kitty)
deck.onSuit = bidder_info[1]
player_order = play.shufflePlayers(player_list, bidder_info)
print(f"{bidder_info[0]} Highest Bidder's hand:")
players[bidder_info[0]].showHand()

# dump cards
players, deck = play.dumpCards(player_order, deck, players)









