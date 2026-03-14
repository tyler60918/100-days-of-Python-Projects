import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')

paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
         ''')

scisscors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
             ''')

playerChoice = int(input("What move do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if playerChoice == 0:
  print(rock)
elif playerChoice == 1:
  print(paper)
elif playerChoice == 2:
  print(scisscors)
else:
  print("Invalid choice")

print("Computer chose:\n")

computerChoice = random.randint(0,2)

if computerChoice == 0:
  print(rock)
elif computerChoice == 1:
  print(paper)
else:
  print(scisscors)

print("\n")
win = True
draw = False

# if playerChoice == 0 and computerChoice == 0:
#   win = False
#   draw = True
# elif playerChoice == 0 and computerChoice == 1:
#   win = False
# elif playerChoice == 0 and computerChoice == 2:
#   win = True
# elif playerChoice == 1 and computerChoice == 0:
#   win = True
# elif playerChoice == 1 and computerChoice == 1: 
#   win = False
#   draw = True
# elif playerChoice == 1 and computerChoice == 2:
#   win = False
# elif playerChoice == 2 and computerChoice == 0:
#   win = False
# elif playerChoice == 2 and computerChoice == 1:
#   win = True
# elif playerChoice == 2 and computerChoice == 2:
#   win = False
#   draw = True

if playerChoice >= 3 or playerChoice < 0:
  print("Invalid choice")
elif playerChoice == 0 and computerChoice == 2:
  win = True
elif playerChoice == 2 and computerChoice == 0:
  win = False
elif computerChoice > playerChoice:
  win = False
elif playerChoice > computerChoice:
  win = True
elif playerChoice == computerChoice:
  win = False
  draw = True

if win:
  print("You win!")
elif draw:
  print("It's a draw.")
else:
  print("You lose :(")