import art
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes in a hand of cards and returns the total score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "It's a Draw."
    elif computer_score == 0:
        return "You lose, opponent has blackjack."
    elif player_score == 0:
        return "You win! You have blackjack."
    elif player_score > 21:
        return "You busted. You lose."
    elif computer_score > 21:
        return "Opponent busted. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def blackjack():
    """Plays a game of blackjack"""

    player_cards = []
    computer_cards = []
    computer_score = -1
    player_score = -1
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            anotherCard = input("Type 'y' to get another card, type 'n' to stand: ").lower()
            if anotherCard == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    print(art.logo)
    blackjack()