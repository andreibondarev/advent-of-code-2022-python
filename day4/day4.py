with open('./input.txt') as f:
  counter = 0

  for line in f:
    sections_1, sections_2 = line.strip().split(',')

    range_1_left, range_1_right = sections_1.split('-')
    range_2_left, range_2_right = sections_2.split('-')

    # We add +1 when converting range to set Python does not include end-range
    # >>> set(range(38, 39))
    # {38}
    range_1_left, range_1_right = int(range_1_left), (int(range_1_right) + 1)
    range_2_left, range_2_right = int(range_2_left), (int(range_2_right) + 1)

    range_1 = range(range_1_left, range_1_right)
    range_2 = range(range_2_left, range_2_right)

    # >>> set(range(38,38))
    # set()
    # ...so we set the default to get set({ 38 })
    set_range_1 = set(range_1) or set({ range_1_left })
    set_range_2 = set(range_2) or set({ range_2_left })

    set_range_1_length = len(set_range_1)
    set_range_2_length = len(set_range_2)
    
    intersection = set_range_1.intersection(set_range_2)

    # Uncomment to get Part 1 answer
    # if (len(intersection) == set_range_1_length) or (len(intersection) == set_range_2_length):
    #   counter += 1

    # Comment out to get Part 1 answer
    if len(intersection) > 0:
      counter += 1

print(counter)
