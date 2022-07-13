from sqlalchemy import false, true
from logo import logo
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score_calculater(deck):
    score = 0
    for card in deck:
        score += card
    return score

def end_checker(deck):
    """Check whether the game ends or not"""
    score = score_calculater(deck)
    if score > 21:
        return true
    else:
        return false

def print_status(user, deck):
    print(f"{user} deck: {deck}")
    print(f"{user} Score: " + str(score_calculater(deck)) + "\n")
    
def winner_checker(player_deck, dealer_deck):
    p_gap = 21 - score_calculater(player_deck)
    d_gap = 21 - score_calculater(dealer_deck)
    
    print("\n===== RESULT =====\n")
    
    if p_gap < d_gap:
        print_status("Player", player_deck)
        print_status("Dealer", dealer_deck)
        print("You Win!")
    elif d_gap == p_gap:
        print_status("Player", player_deck)
        print_status("Dealer", dealer_deck)
        print("Tie the game")
    else:
        print_status("Player", player_deck)
        print_status("Dealer", dealer_deck)
        print("You Lose")

def play_game(player_deck, dealer_deck):
    answer = ""
    print(f"Your deck: {player_deck}")
    while (answer != "2"):
        answer = input("1. Hit   2. Stand\nAnswer: ")
        if answer == "1":
            player_deck.append(deal_card())
            print_status("Player", player_deck)
            if score_calculater(player_deck) == 21:
                print_status("Player", player_deck)
                print("JUST 21!!\nYou Win!")
                return
            
        if end_checker(player_deck) == true:
            print_status("Player", player_deck)
            print("You lose")
            return
    
    while (score_calculater(dealer_deck) < 17):
        dealer_deck.append(deal_card())
        if end_checker(dealer_deck) == true:
            print("You Win!")
            return
    
    winner_checker(player_deck, dealer_deck)
    
        

if __name__ == '__main__':
    print(f"{logo}\n")

    player_deck = []
    dealer_deck = []
    
    for _ in range(2):
        player_deck.append(deal_card())
        dealer_deck.append(deal_card())
        
    play_game(player_deck, dealer_deck)