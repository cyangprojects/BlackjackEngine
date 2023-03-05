from BlackJackEngine import BlackjackEngine
from BlackJackPlayer import BlackjackPlayer
from AutomaticBlackjackPlayer import AutomaticBlackjackPlayer
from InteractiveBlackjackPlayer import InteractiveBlackjackPlayer
import random

sum = 0
hands_played = 0
for i in range(1000):

    bj = BlackjackEngine(8)
    bob = AutomaticBlackjackPlayer("Timothy Herchen, M 19", 10000000)
    bj.add_player(bob)
    bj.play_game(False)
    sum += bob.balance
    hands_played += bob.hands_played
print(sum)
print(hands_played)
bob.records.close()