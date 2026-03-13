print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extraCheese = input("Do you want extra cheese? Y or N: ")

total = 0

if size == "S":
  total += 15
  if pepperoni == "Y":
    total += 2
elif size == "M":
  total += 20
  if pepperoni == "Y":
    total += 3
elif size == "L":
  total += 25
  if pepperoni == "Y":
    total += 3
else:
  print("Invalid size.")

if extraCheese == "Y":
  total += 1

print(f"Your total bill is: ${total}")
