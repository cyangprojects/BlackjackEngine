from Card import Card
class Hand:
    cards: list[Card]
    bet: int

    def __init__(self, cards = None, bet: int = 0): #Default values
        self.cards = cards if cards else []
        self.bet = bet
        self.hasHit = False
    def contains_ace(self):
        contains_ace = False
        for card in self.cards:
            if card.value == 'A':
                contains_ace = True
        return contains_ace
    def sort(self):
        return sorted(self.cards, key=Card.get_value)
    def get_card(self, index: int):
        return self.cards[index]
    def add_card(self, card: Card):
        self.cards.append(card)
    def busted(self):
        return self.get_hand_value() > 21
    def __str__(self):
         return '\n'.join(map(str, self.cards)) + f"\nHand Value: {self.get_hand_value()}"
    def __repr__(self):
        return str(self)
    def get_hand_value(self):
        value = sum(map(Card.get_value, self.cards)) #Passes the function itself, not calling it so parenthesis not needed
        num_aces = len(list(filter(lambda card: card.value == 'A', self.cards)))
        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1
        return value
    def can_split(self):
        return len(self.cards) == 2 and self.cards[0] == self.cards[1]
    def split_ace_hand(self):
        return len(self.cards) == 1 and self.cards[0].value == 'A'
    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_hand_value() == 21