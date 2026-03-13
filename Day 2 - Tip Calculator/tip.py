print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tipPercent = int(input("What percentage of tip would you like to give? "))
numPeople = int(input("How many people to split the bill? "))

totalAfterTip = total + total * (tipPercent / 100)
totalPerPerson = totalAfterTip / numPeople
formattedTotalPerPerson = round(totalPerPerson, 2)

print(f"Each person should pay ${formattedTotalPerPerson}")