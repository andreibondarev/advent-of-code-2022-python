# Rock: A, X - 1 point
# Paper: B, Y - 2 points
# Scissors: C, Z - 3 points

# Yes, this is a shortcut, but not against the rules.
scenarios = {
  'A X': 3, # scissors -> loss
  'A Y': 4, # rock -> draw
  'A Z': 8, # paper -> win
  'B X': 1, # rock -> loss
  'B Y': 5, # paper -> draw
  'B Z': 9, # scissors -> win
  'C X': 2, # paper -> loss
  'C Y': 6, # scissors -> draw
  'C Z': 7, # rock -> win
}

score = 0

with open('./input.txt') as f:
  for line in f:
    score += scenarios.get(line.strip())

print(score)