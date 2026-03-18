import random

import hangman_art
from hangman_words import word_list

stages = hangman_art.stages
logo = hangman_art.logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:
    display = ""

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in correct_letters or  guessed_letter in incorrect_letters:
        print(f"Already guessed {guessed_letter}")
    else:
        for letter in chosen_word:
            if guessed_letter == letter:
                correct_letters.append(letter)
                display += letter
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print(display)

        if guessed_letter not in chosen_word:
            print(f"{guessed_letter} is not in the word. You lose one life.")
            lives -= 1
            incorrect_letters.append(guessed_letter)

        print(stages[lives])

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was {chosen_word}")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")
    