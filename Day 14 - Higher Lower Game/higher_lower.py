import art
import game_data
import random

data = game_data.data
playing = True
score = 0

choice_a = random.choice(data)
print(art.logo)
while playing:

    choice_b = random.choice(data)

    print(f"Compare A: {choice_a["name"]}, a {choice_a["description"]}, from {choice_a["country"]}.\n")

    print(f"{art.vs}\n")

    print(f"Against B: {choice_b["name"]}, a {choice_b["description"]}, from {choice_b["country"]}.")

    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    winner = ""
    if choice_a["follower_count"] > choice_b["follower_count"]:
        winner = "A"
    elif choice_a["follower_count"] < choice_b["follower_count"]:
        winner = "B"

    print(art.logo)
    if player_choice == winner:
        score += 1
        print(f"You're correct! {choice_a["name"]} has {choice_a["follower_count"]} million followers and {choice_b["name"]} has {choice_b["follower_count"]} million followers. Current score: {score}")
        choice_a = choice_b
    else:
        print(f"You're incorrect. {choice_a["name"]} has {choice_a["follower_count"]} million followers and {choice_b["name"]} has {choice_b["follower_count"]} million followers. Final score: {score}")
        playing = False