def tail_and_head_touching(coords_head, coords_tail):
  return (abs(coords_head[0] - coords_tail[0]) <= 1) and (abs(coords_head[1] - coords_tail[1]) <= 1)

def process_move(direction, distance, coords_head, coords_tail):
  print(coords_head)
  print(coords_tail)

  if direction == 'L':
    coords_head = (
      (coords_head[0] - distance), # Move left on the X axis
      coords_head[1]
    )

    if not tail_and_head_touching(coords_head, coords_tail):
      coords_tail = (
        (coords_head[0] - distance + 2), # Move left on the X axis (offset by 1)
        coords_head[1]
      )

  elif direction == 'R':
    coords_head = (
      (coords_head[0] + distance), # Move right on the X axis
      coords_head[1] 
    )

    if not tail_and_head_touching(coords_head, coords_tail):
      coords_tail = (
        (coords_head[0] + distance - 2), # Move left on the X axis (offset by 1)
        coords_head[1]
      )

  elif direction == 'U':
    coords_head = (
      coords_head[0],
      (coords_head[1] + distance) # Move up on the Y axis
    )

    if not tail_and_head_touching(coords_head, coords_tail):
      coords_tail = (
        coords_head[0],
        (coords_head[1] + distance - 2)  # Move up on the Y axis
      )

  elif direction == 'D':
    coords_head = (
      coords_head[0],
      (coords_head[1] - distance) # Move down on the Y axis
    )

    if not tail_and_head_touching(coords_head, coords_tail):
      coords_tail = (
        coords_head[0],
        (coords_head[1] - distance + 2) # Move down on the Y axis
      )

  return coords_head, coords_tail

with open('./input.txt') as f:
  # x,y coords
  coords_tail = (0, 0)
  coords_head = (0, 0)

  positions_visited = []

  for line in f:
    direction, distance = line.strip().split(' ')
    distance = int(distance)

    # TODO: The move must be processed per each incremental move
    for distance_unit in range(1, (distance + 1)):
      coords_head, coords_tail = process_move(direction, 1, coords_head, coords_tail)
      positions_visited.append(coords_tail)

print(len(set(positions_visited)))