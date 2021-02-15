import deck
import player
import play


group = 2
players = {}
player_list = []
# group = input("number of players>")
# for i in range(0, int(group)):
    # name = input("Player Name>")
    # players[i] = player.Player(name)
    # player_list.append(i)

players["Todd"] = player.Player("Todd")
player_list.append("Todd")
players["Anish"] = player.Player("Anish")
player_list.append("Anish")
kitty = player.Player("Kitty")

deck = deck.Deck()
deck.shuffle(7)

# opening deal
print("Opening deal!  3 cards to each player, and the Kitty")
for p in players:
    players[p].draw(deck, 3)
    # print(f"{players[p].name}\'s hand")
    # players[p].showHand()

kitty.draw(deck, 3)
print("Kitty Drawn, 3 Cards Face Down")
# kitty.showHand()

print("Opening deal!  Now, 2 cards to each player.")
for p in player_list:
    players[p].draw(deck, 2)
    print(f"{players[p].name}\'s hand")
    players[p].showHand()

# start game
# ask to flip a card to determine suit, or just open to bidding
players, deck, player_order = play.flip(players, player_list, kitty, deck)

# dump cards
players, deck = play.dumpCards(player_order, deck, players)









