from Card import Card
import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

def shuffle_in_place(arr: list[int]):
    for i in range(len(arr) - 1, -1, -1):
        j = int(random.random() * (i+1))
        swp = arr[i]
        arr[i] = arr[j]
        arr[j] = swp


class Deck:
    deck: list[Card]
    def __init__(self, numDecks: int):
        self.deck = []
        self.create_deck(numDecks)
    def create_deck(self, numDecks: int):
        for i in range(numDecks):
            for value in values:
                for suit in suits:
                    self.deck.append(Card(value, suit))
    def shuffle_deck(self):
        shuffle_in_place(self.deck)
    def deal_card(self):
        return self.deck.pop()