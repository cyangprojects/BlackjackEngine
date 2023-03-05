from Card import Card
from Hand import Hand

class BlackjackPlayer:
    name: str
    balance: int
    hands_played: int
    hands: list[Hand]
    dealer_card: Card
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance
        self.hands_played = 0
        self.records = open(f"{self.name} Records.txt", "w") 
        self.hands = [Hand()]
        self.dealer_card = None #One card
    def update_records(self,  player_hand_value: int, dealer_hand_value: int, result: str):
        self.records.write(f"\n Player Hand Value: {player_hand_value}, Dealer Hand Value: {dealer_hand_value}, Result: {result}, Player balance: {self.balance}" )
        
        
        
    def clear_hands(self):
        self.dealer_card = None
        self.hands = [Hand()]
    def num_hands(self):
        return len(self.hands)
    def split_hand(self, hand: Hand):
        assert (self.num_hands() < 4)
        index = self.hands.index(hand)
        new_hands = [Hand(cards = [hand.get_card(1-i)], bet=hand.bet) for i in range(2)]    
        self.hands = [*self.hands[:index], *new_hands, *self.hands[index+1:] ] #splat makes it so the elements go inside the new array without the old array
    def show_new_card(self, card: Card, hand: Hand):
        hand.add_card(card)
    def show_dealer_card(self, card: Hand):
        self.dealer_card = card
    def next_play(self, hand: Hand):
        raise NotImplementedError()
    def input_bet(self):
        raise NotImplementedError()
    def input_participation(self):
        raise NotImplementedError()
    def all_busted(self):
        return all(hand.busted() for hand in self.hands)
