from player import Player

# ===========================================================================
# Description: a card player with money and a hand of stack_of_cards
#
# State Attributes
#    name - string - the name of the player
#    hand - StackOfCards - a bunch of cards
#    money - integer - how much money player has
# Methods
#    introduce() - prints out message "Hi, my name is ..."
#    __str__() - returns a string ex. 'Joe: 4d 7c 10s Ah'
#    getName() - returns the name of the player
#    getMoney() - returns the money balance
#    getCard(pos) - returns a Card at the pos number
#    addCard(card) - add card to the player's hand of stack_of_cards
#    removeCard(pos) - removes a card at the pos number
#    addMoney(amt) - add amt to player's money
# ===========================================================================


class PokerPlayer(Player):

    # inputs:
    #    name - string for the player's name
    #    amount - integer for how much money the player has
    #    cards - a StackOfCards
    def __init__(self, name, amount, cards):
        # Constructor
        self.name = name
        self.money = amount
        self.hand = cards

    def askHoldChoice(self):
        holdcards = input("What cards do you want to hold(ex. 1,2,3,4), if none hit enter: ")
        ls_cards = list(holdcards)
        cards_held = [int(item) - 1 for item in ls_cards if item in ['0', '1', '2', '3', '4', '5']]
        return cards_held

