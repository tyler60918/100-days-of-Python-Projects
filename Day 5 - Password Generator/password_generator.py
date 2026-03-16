import random

letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

print("Welcome to the password generator!")
numLetters = int(input("How many letters would you like in your password?\n"))
numNumbers = int(input("How many numbers would you like in your password?\n"))
numSymbols = int(input("How many symobls would you like in your password?\n"))
scramble = input("Do you want the password scrambled? y or n: \n").lower()

# Easy Level / Non-Scrambled
if scramble == "n":
  for i in range(numLetters):
    password += random.choice(letters)
  for i in range(numNumbers):
    password += random.choice(numbers)
  for i in range(numSymbols):
    password += random.choice(symbols)

# Hard Level / Scrambled
elif scramble == "y":
  totalLength = numLetters + numNumbers + numSymbols
  scrambledList = [''] * totalLength
  availableIndexes = [0] * totalLength
  for i in range(totalLength):
    availableIndexes[i] = i
  for i in range(numLetters):
    randIndex = random.choice(availableIndexes)
    scrambledList[randIndex] = random.choice(letters)
    availableIndexes.remove(randIndex)
  for i in range(numNumbers):
    randIndex = random.choice(availableIndexes)
    scrambledList[randIndex] = random.choice(numbers)
    availableIndexes.remove(randIndex)
  for i in range(numSymbols):
    randIndex = random.choice(availableIndexes)
    scrambledList[randIndex] = random.choice(symbols)
    availableIndexes.remove(randIndex)
  for char in scrambledList:
    password += char
else:
  print("Invalid response")
print(f"Your password is: {password}")

# Hard Level / Scrambled (simpler)
if scramble == "y":
  passwordList = []
  password = ""
  for i in range(numLetters):
    passwordList += random.choice(letters)
  for i in range(numNumbers):
    passwordList += random.choice(numbers)
  for i in range(numSymbols):
    passwordList += random.choice(symbols)
  random.shuffle(passwordList)

  for c in passwordList:
    password += c
  print(f"Your password is: {password}")