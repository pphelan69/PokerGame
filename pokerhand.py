"""
Edited Mar 4, 2020

@author: Ria Phelan
"""

from stack_of_cards import StackOfCards

# ===========================================================================
# Description: A list of Card; used for a player's hand of cards
#
# State Attributes
#     - cards - list of card; starts out empty from inherited StackOfCards constructor
# Methods
#     - isRoyalFlush() - randomly shuffle all the card in the list
#     - isStraightFlush() - deal the 'top' card from the hand/deck
#     - add(card) - add Card to the list of cards
#     - remove(pos) - remove and return Card at pos number
#     - size() - size of hand
#     - getCard(pos) - returns a Card at the 'pos'
#     - __str__() - returns string of all the cards in the hand like '4♣ 10♥ A♠'
# ===========================================================================


class PokerHand(StackOfCards):

    def sort(self):
        sorted_hand = sorted(self.cards, key=lambda x: x.getValue(), reverse=False)

        for i in range(len(sorted_hand)):
            self.cards[i] = sorted_hand[i]

        return self.cards

    def _getCardValues(self):
        card1_value = self.cards[0].getValue()
        card2_value = self.cards[1].getValue()
        card3_value = self.cards[2].getValue()
        card4_value = self.cards[3].getValue()
        card5_value = self.cards[4].getValue()
        list_card_values = [card1_value, card2_value, card3_value, card4_value, card5_value]
        return list_card_values

    def _getCardSuits(self):
        card1_suit = self.cards[0].getSuit()
        card2_suit = self.cards[1].getSuit()
        card3_suit = self.cards[2].getSuit()
        card4_suit = self.cards[3].getSuit()
        card5_suit = self.cards[4].getSuit()
        list_card_suits = [card1_suit, card2_suit, card3_suit, card4_suit, card5_suit]
        return list_card_suits

    def handTyoe(self):

        list_card_values = PokerHand._getCardValues(self)
        list_card_suits = PokerHand._getCardSuits(self)
        card_sum = sum(list_card_values)

        all_same_suite = False
        if list_card_suits[0] == list_card_suits[1]:
            if list_card_suits[1] == list_card_suits[2]:
                if list_card_suits[2] == list_card_suits[3]:
                    if list_card_suits[4] == list_card_suits[5]:
                        all_same_suite = True

        straight = False
        if list_card_values[0] + 1 == list_card_values[1]:
            if list_card_values[1] + 1 == list_card_values[2]:
                if list_card_values[2] + 1 == list_card_values[3]:
                    if list_card_values[3] + 1 == list_card_values[4]:
                        straight = True

        four_kind = False
        if list_card_values.count(list_card_values[4-1]) == 4:
            four_kind = True

        three_kind = False
        if list_card_values.count(list_card_values[3-1]) == 3:
            three_kind = True

        two_kind = False
        for item in list_card_values:
            if list_card_values.count(item) == 2:
                two_kind = True

        full_house = three_kind and two_kind

        two_pair = False
        pair_count = 0
        for item in list_card_values:
            if list_card_values.count(item) == 2:
                pair_count = pair_count + 1
                if pair_count == 4:
                    two_pair = True

        royal_pair = False
        for item in list_card_values:
            if item > 10:
                if list_card_values.count(item) == 2:
                    royal_pair = True

        if card_sum == 60 and all_same_suite:
            return "Royal Flush"
        elif all_same_suite and straight:
            return "Straight Flush"
        elif four_kind:
            return "Four of a Kind"
        elif full_house:
            return "Full House"
        elif all_same_suite:
            return "Flush"
        elif straight:
            return "Straight"
        elif three_kind:
            return "Three of a kind"  # Works
        elif two_pair:
            return "Two Pairs"  # Works
        elif royal_pair:
            return "Pair (Jacks or better)"  # Works
        else:
            return "Nothing"


























