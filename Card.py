class Card:
    value: str
    suit: str

    def __init__(self, value: str, suit: str):
        self.suit = suit
        self.value = value
    def get_value(self):
        if self.value in ['J', 'Q', 'K', 'T']: #Keep in mind A is special case
            return 10
        elif self.value == 'A':
            return 11
        else:
            return int(self.value)

    def __repr__(self):
        return str(self)
    #str(Card())
    def __str__(self): 
        return f"Card ({self.value}, {self.suit})"
    def __eq__(self, card):
        return self.get_value() == card.get_value()
    def __neq__(self, card):
        return not self.equals(card)