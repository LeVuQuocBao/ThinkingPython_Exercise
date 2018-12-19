from random import shuffle


class Card(object):
    def __init__(self, rank, suit):
        assert rank < 14 and rank > 0 and suit < 4 and suit >= 0, 'Invalid card'
        self.rank = rank
        self.suit = suit

    rank_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
    suit_list = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __str__(self):
        return self.rank_dict[self.rank] + ' of ' + self.suit_list[self.suit]

    def __lt__(self, other):
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        if self.__eq__(other):
            return 0
        return t1 < t2

    def __eq__(self, other):
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        return t1 == t2


class Deck(object):
    def __init__(self):
        self.cards = []
        for Csuit in range(4):
            for Crank in range(1, 14):
                self.cards.append(Card(Crank, Csuit))

    def __str__(self):
        strofdeck = []
        for card in self.cards:
            strofdeck.append(str(card))
        if len(strofdeck) == 0:
            return 'Null'
        return '\n'.join(strofdeck)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, othercard):
        self.cards.append(othercard)

    def suffle_deck(self):
        shuffle(self.cards)

    def sort_deck(self, arg=None):
        if arg == 'reverse':
            reverse = True
        else:
            reverse = False
        self.cards.sort(reverse=reverse)

    def move_n_card(self, deck, n):
        for i in range(n):
            self.add_card(deck.pop_card())
    def deal_hand(self,n_hand,n_card):
        handlist=[]
        for i in range(n_hand):
            handlist.append(Hand())
            handlist[i].move_n_card(self,n_card)
        return handlist

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label


fulldeck = Deck()
# hand = Hand('new_hand')
# hand.move_n_card(fulldeck, 2)
# print(hand)
# fulldeck.move_n_card(hand, 2)
# print(hand)
fulldeck.suffle_deck()
players=fulldeck.deal_hand(2,3)
print('players[1]')
print(players[0])
print('players[2]')
print(players[1])
print('Remain deck')
print(fulldeck)
# fulldeck = Deck()
# print(fulldeck)
# # fulldeck.pop_card()
# # print(fulldeck)
# # # fulldeck.add_card(Card(13,3))
# # # print(fulldeck)
# fulldeck.suffle_deck()
# print(fulldeck)
# print('\n')
# fulldeck.sort_deck('reverse')
# print(fulldeck)
