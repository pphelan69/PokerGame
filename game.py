
from pokercard import PokerCard
from stack_of_cards import StackOfCards
from pokerhand import PokerHand
from pokerplayer import PokerPlayer


def PlayRound(player, deck):

    print("Cards Dealt: " + player.hand.__str__())

    # Deal 2nd hand of cards
    hand2 = PokerHand()
    cards_held = player.askHoldChoice()

    for i in range(player.hand.size()):
        if i in cards_held:
            hand2.add(player.getCard(i))
        else:
            hand2.add(deck.deal())

    hand2.sort()
    print(hand2.__str__())

    # Check poker score of hand2
    handType = hand2.handTyoe()
    print("You got: " + handType)

    if handType == "Royal Flush":
        player_win = 250
    elif handType == "Straight Flush":
        player_win = 50
    elif handType == "Four of a Kind":
        player_win = 25
    elif handType == "Full House":
        player_win = 9
    elif handType == "Flush":
        player_win = 6
    elif handType == "Straight":
        player_win = 4
    elif handType == "Three of a kind":
        player_win = 3
    elif handType == "Two Pairs":
        player_win = 2
    elif handType == "Pair (Jacks or better)":
        player_win = 1
    else:
        player_win = 0

    player.addMoney(player_win-1)  # Need to subtract 1 credit as each play costs 1 credit.
    print("You won these many credits: " + str(player_win))

    print("Credits remaining: " + str(player.getMoney()))

    # Ask if you want to play again
    playAgain = input("Would you like to play again? (y/n)? ")

    if player.getMoney() == 0:
        print("You have no more credits, GAME OVER")
    elif playAgain == 'y' or playAgain == 'Y':
        cards = PokerHand()
        cards.add(deck.deal())
        cards.add(deck.deal())
        cards.add(deck.deal())
        cards.add(deck.deal())
        cards.add(deck.deal())
        cards.sort()
        player = PokerPlayer(player.getName(), player.getMoney(), cards)

        deck = StackOfCards()

        ls_suit = ['♥', '♦', '♣', '♠']
        ls_rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for rank in ls_rank:
            for suit in ls_suit:
                deck.add(PokerCard(rank, suit))




def PokerGame():

    # Create the shuffled deck of Cards
    deck = StackOfCards()

    ls_suit = ['♥', '♦', '♣', '♠']
    ls_rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for rank in ls_rank:
        for suit in ls_suit:
            deck.add(PokerCard(rank, suit))
    deck.shuffle()

    # Poker Player initializing
    name = input("What is your name? ")
    str_amount = input("How many credits you have? ")
    amount = int(str_amount)
    print("You have " + str(amount) + " credits.")
    cards = PokerHand()
    cards.add(deck.deal())
    cards.add(deck.deal())
    cards.add(deck.deal())
    cards.add(deck.deal())
    cards.add(deck.deal())
    cards.sort()

    player = PokerPlayer(name, amount, cards)
    PlayRound(player, deck)


PokerGame()





