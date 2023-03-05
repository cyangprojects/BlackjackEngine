from BlackJackPlayer import BlackjackPlayer
from Hand import Hand

class InteractiveBlackjackPlayer(BlackjackPlayer):
    def input_participation(self):
        return input(f"{self.name}: Do you want to play BlackJack? ('Y' or 'N)").upper()
    def input_bet(self):
        bet = self.balance + 1
        while (self.balance - bet < 0):
            bet = int(input(f"Your balance is: {self.balance}. How much do you want to bet?"))
        return bet
    def next_play(self, hand: Hand, showText = True):
        print("\n" + self.name + "'s Hand:")
        print(hand)
        if hand.is_blackjack():
            return "BJ"
        if hand.get_hand_value() < 21:
            output = "\nWould you like to hit or stand? ('H' for hit,'S' for stand)"
            if (self.balance - (int(hand.bet) * 2) > 0 and not hand.hasHit):
                output = "\nWould you like to hit, double, or stay? ('H' for hit,'S' for stand, 'D' for double)"
                if (hand.can_split() and (self.balance - (int(hand.bet) * 2) )):
                    output = "\nWould you like to hit, double, or stay? ('H' for hit,'S' for stand, 'D' for double, 'P' for split)"
            return input(output).upper()


