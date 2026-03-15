studentScores = [98, 72, 89, 70, 99, 100, 52, 88, 90, 95, 96, 91, 84, 56, 88, 89, 62]

totalScore = sum(studentScores)

# or manually

sum = 0
for score in studentScores:
  sum += score

# finding max score

maxScore = 0
for score in studentScores:
  if score > maxScore:
    maxScore = score
print(maxScore)

# or

maxScore = max(studentScores)