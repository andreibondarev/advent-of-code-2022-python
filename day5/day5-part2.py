#                     [L]     [H] [W]
#                 [J] [Z] [J] [Q] [Q]
# [S]             [M] [C] [T] [F] [B]
# [P]     [H]     [B] [D] [G] [B] [P]
# [W]     [L] [D] [D] [J] [W] [T] [C]
# [N] [T] [R] [T] [T] [T] [M] [M] [G]
# [J] [S] [Q] [S] [Z] [W] [P] [G] [D]
# [Z] [G] [V] [V] [Q] [M] [L] [N] [R]
#  1   2   3   4   5   6   7   8   9 

crates = [
  [             'S' ,  'P', 'W' , 'N', 'J', 'Z' ], # 1
  [                               'T', 'S', 'G' ], # 2
  [                   'H' , 'L' , 'R', 'Q', 'V' ], # 3
  [                         'D' , 'T', 'S', 'V' ], # 4
  [       'J' , 'M' , 'B' , 'D' , 'T', 'Z', 'Q' ], # 5
  [ 'L' , 'Z' , 'C' , 'D' , 'J' , 'T', 'W', 'M' ], # 6
  [       'J' , 'T' , 'G' , 'W' , 'M', 'P', 'L' ], # 7
  [ 'H' , 'Q' , 'F' , 'B' , 'T' , 'M', 'G', 'N' ], # 8
  [ 'W' , 'Q' , 'B' , 'P' , 'C' , 'G', 'D', 'R' ]  # 9
]

assert(len(crates) == 9)

from itertools import islice
from collections import deque 

with open('./input.txt') as f:

  # Skip the crates setup since it's hard-coded above
  for line in islice(f, 10, None):
    # Remove "move " from the beginning
    string = line.strip().replace('move ', '')

    print(line.strip())

    quantity, rest = string.split(' from ')
    
    origin, destination = rest.split(' to ')

    origin_idx = int(origin) - 1
    destination_idx = int(destination) - 1

    origin_array = crates[origin_idx]
    destination_array = crates[destination_idx]

    # Slice off the array of crates being moved
    crates_in_flight = origin_array[:int(quantity)]

    # For each crate -> pop them off and insert to the beginning of the destination array
    while len(crates_in_flight) > 0:
      crate_in_flight = crates_in_flight.pop()
      origin_array.remove(crate_in_flight)

      destination_array.insert(0, crate_in_flight)

  top_crates = crates[0][0] + crates[1][0] + crates[2][0] + crates[3][0] + crates[4][0] + crates[5][0] + crates[6][0] + crates[7][0]  + crates[8][0]

print(top_crates)
