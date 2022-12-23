# Rock: A, X
# Paper: B, Y
# Scissors: C, Z

# Yes, this is a shortcut, but not against the rules.
scenarios = {
  'A X': 4, # draw
  'A Y': 8, # win
  'A Z': 3, # loss
  'B X': 1, # loss
  'B Y': 5, # draw
  'B Z': 9, # win
  'C X': 7, # win
  'C Y': 2, # loss
  'C Z': 6  # draw
}

score = 0

with open('./input.txt') as f:
  for line in f:
    score += scenarios.get(line.strip())

print(score)