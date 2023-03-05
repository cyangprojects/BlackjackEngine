from BlackJackPlayer import BlackjackPlayer
from Deck import Deck
from Hand import Hand

import math


#Cant double after hitting
#Cant double after splitting?

def get_log_function(show_text: bool):
    return lambda f: print(f()) if show_text else lambda f : 0 




class BlackjackEngine:
    deck: Deck
    players: list[BlackjackPlayer]
    dealer_hand:  Hand
    def __init__(self, numDecks: int):
        self.deck = Deck(numDecks)
        self.deck.shuffle_deck()
        self.players = []
        self.dealer_hand = Hand()
    def add_player(self, player: BlackjackPlayer):
        self.players.append(player)
    def add_dealer_hand(self):
        self.dealer_hand.add_card(self.deck.deal_card())
    def output_dealer_hand(self):
        print("Dealing...")
        print("\nDealer is showing:")
        print(self.dealer_hand.get_card(0)) #First card is the one face up
        print("[Hidden]")
    def player_move(self, move: str, hand: Hand, player: BlackjackPlayer):
        if move == "S" or move == "BJ":
            return False
        if move == "H":
            if hand.split_ace_hand(): #If hand is a split ace
                self.player_hit(hand)
                hand.hasHit = True
                return True
            self.player_hit(hand)
            return not hand.busted()
        elif move == "D":
            if not hand.hasHit:
                hand.bet = 2 * int(hand.bet)
                self.player_hit(hand)
                return False
        elif (move == "P" and (player.balance - (int(hand.bet) * 2)) > 0):
            if (hand.can_split()):
                player.split_hand(hand)
                return False
        return True
    def player_hit(self, hand):
        hand.add_card(self.deck.deal_card())
    
    def dealer_hits(self, showText: bool):
        log = get_log_function(showText)
        while self.dealer_hand.get_hand_value() < 17:
            log(lambda: f"\nDealer hits... \n")
            self.add_dealer_hand()
            if showText:
                print(self.dealer_hand)


    def evaluate_game(self, playerList, showText:bool):
        log = get_log_function(showText)
        for player in playerList:
            for hand in player.hands:
                win_fraction = 0.0
                if hand.is_blackjack():
                    if self.dealer_hand.is_blackjack():
                        log(lambda: f"{player.name} pushes! Bet is returned")
                    else:
                        win_fraction = 1.5
                        log(lambda: f"{player.name} BlackJack!")     
                elif hand.busted():
                    win_fraction = -1
                    log(lambda: f"{player.name} busted!")
                elif self.dealer_hand.busted():
                    win_fraction = 1
                    log(lambda: f"Dealer busted!")
                else:
                    difference = hand.get_hand_value() - self.dealer_hand.get_hand_value()

                    if difference > 0:
                        win_fraction = 1
                        log(lambda: f"{player.name} wins!")
                    elif difference < 0:
                        win_fraction = -1
                        log(lambda: f"{player.name} loses!")
                    else:
                        log(lambda: f"{player.name} pushes! Bet is returned")
                player.balance = player.balance + int(win_fraction * hand.bet)
                log(lambda: f"{player.name}'s new balance is {player.balance}")
                player.update_records(hand.get_hand_value(), self.dealer_hand.get_hand_value(), "Win" if win_fraction >= 1 else "Lose" if win_fraction == -1 else "Tie")
                
    


    def dealer_deals(self):
        currentPlayers = []
        for player in self.players:
            player.clear_hands()
            if player.input_participation() == 'Y':
                    player.hands_played += 1
                    currentPlayers.append(player)
                    player.hands[0].bet = player.input_bet()
                    player.show_new_card(self.deck.deal_card(), player.hands[0])
            self.add_dealer_hand()
            for player in currentPlayers:
                player.show_dealer_card(self.dealer_hand.get_card(0))
                player.show_new_card(self.deck.deal_card(), player.hands[0])
            self.add_dealer_hand()
        return currentPlayers



    def play_round(self, showText: bool):
        self.dealer_hand = Hand()
        log = get_log_function(showText)
        currentPlayers = self.dealer_deals()
        if currentPlayers == []:
            print("No players agreed to play\n")
        if showText:
            self.output_dealer_hand()
        for player in currentPlayers:
            hand_index = 0
            while hand_index < len(player.hands):
                hand = player.hands[hand_index]
                playerHasActionsLeft = True
                while playerHasActionsLeft:
                    next_play = player.next_play(hand, showText).upper()
                    if next_play == 'P':
                        hand_index-= 1
                    playerHasActionsLeft = self.player_move(next_play, hand, player)
                if showText:
                    print(hand)
                hand_index += 1
        log(lambda: f"\nDealer shows... \n" + str(self.dealer_hand))
        if not all(player.all_busted() for player in currentPlayers):
                self.dealer_hits(showText) 
        self.evaluate_game(currentPlayers, showText)



    def play_game(self, showText: bool):
        while len(self.deck.deck) > 20:
            self.play_round(showText)