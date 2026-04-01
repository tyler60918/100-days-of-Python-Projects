import art
import random

print(art.logo)
print("Welcome to Number Guesser!")
print("Im thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

correct_number = random.randint(1, 100)

win = False
while lives > 0 and win != True:
    print(f"You have {lives} lives remaining to guess the correct number.")
    guess = int(input("Make a guess: "))

    if guess > correct_number:
        print("Too high, guess again.")
        lives -= 1
    elif guess < correct_number:
        print("Too low, guess again.")
        lives -= 1
    else:
        print("Thats correct! You win!")
        win = True
if lives < 1:
    print(f"You lose, the correct number was {correct_number}")