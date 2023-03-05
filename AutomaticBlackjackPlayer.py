from BlackJackPlayer import BlackjackPlayer
from Hand import Hand

pairSplitString = """
pppppphhhh
pppppphhhh
hhhpphhhhh
ddddddddhh
ppppphhhhh
ppppppphhh
pppppppppp
pppppsppss
ssssssssss
pppppppppp""".strip()
#2-2 to A-A
aceSplitString = """
hhhddhhhhh
hhhddhhhhh
hhdddhhhhh
hhdddhhhhh
hddddhhhhh
sddddsshhh
ssssssssss
ssssssssss
ssssssssss""".strip()
#A-2 to A-10
hardTotalSplitString = """
hhhhhhhhhh
dddddhhhhh
ddddddddhh
dddddddddd
hhssshhhhh
ssssshhhhh
ssssshhhhh
ssssshhhhh
ssssshhhhh
ssssssssss""".strip()
#A-8 is the first sentence, 17+ is last sentence
pairSplitList = pairSplitString.split('\n')
aceSplitList = aceSplitString.split('\n')
hardTotalSplitList = hardTotalSplitString.split('\n')

def get_log_function(show_text: bool):
    return lambda f: print(f()) if show_text else lambda f : 0 


class AutomaticBlackjackPlayer(BlackjackPlayer):
    def input_bet(self):
        return 1 # temporary
    def input_participation(self):
        return 'Y'
    def next_play(self, hand: Hand, showText: bool):
        if hand.is_blackjack():
            return "BJ"
        log = get_log_function(showText)
        if (showText):
            print("\n" + self.name + "'s Hand:")
            print(hand)
        dealer_index = self.dealer_card.get_value()
        play = None
        if hand.can_split() and self.num_hands() < 4:
            split_card_index = hand.get_card(0).get_value()
            log(lambda: f"{pairSplitList[split_card_index-2][dealer_index-2]}")
            play = pairSplitList[split_card_index-2][dealer_index-2]
        elif (hand.contains_ace() and len(hand.cards)) == 2:
            for i, card in enumerate(hand.cards):
                if card.value != 'A':
                    non_ace_index = card.get_value()
            log(lambda: f"{aceSplitList[non_ace_index-2][dealer_index-2]}")
            play = aceSplitList[non_ace_index-2][dealer_index-2]
        else:
            if hand.get_hand_value() <= 8:
                log(lambda: f"{hardTotalSplitList[0][dealer_index-2]}")
                play = hardTotalSplitList[0][dealer_index-2]
                
            elif hand.get_hand_value() >= 17:
                log(lambda: f"{hardTotalSplitList[9][dealer_index-2]}")
                play = hardTotalSplitList[9][dealer_index-2]
            else:
                log(lambda: f"{hardTotalSplitList[hand.get_hand_value()-8][dealer_index-2]}")
                play = hardTotalSplitList[hand.get_hand_value() - 8][dealer_index-2]
        if play == 'd' and hand.hasHit:
            play = 'h'
        return play
