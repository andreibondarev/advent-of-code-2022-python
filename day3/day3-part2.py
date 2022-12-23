def get_priority(letter):
  if letter.isupper():
    return ord(letter) - 38
  else:
    return ord(letter) - 96

with open('./input.txt') as f:
  total = 0

  # Get the first line
  line = next(f)

  while line:
    rucksack_1 = line.strip()
    # Get the second line
    rucksack_2 = next(f).strip()
    # Get the third line
    rucksack_3 = next(f).strip()

    intersection_dict = set(rucksack_1) & set(rucksack_2) & set(rucksack_3)

    # Determine the priority
    letter = next(iter(intersection_dict))
    priority = get_priority(letter)

    # Sum up the results
    total += priority

    # Get the next line (first elf of the next group) to satify the while loop above
    line = next(f, None)
    
print(total)