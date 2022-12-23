def get_priority(letter):
  if letter.isupper():
    return ord(letter) - 38
  else:
    return ord(letter) - 96

with open('./input.txt') as f:
  total = 0

  for line in f:
    rucksack_content = line.strip()

    # 1: Split the string down the middle
    compartment_1, compartment_2 = rucksack_content[:len(rucksack_content)//2], rucksack_content[len(rucksack_content)//2:]

    # 2: Find the intersecting letter
    intersection_dict = set(compartment_1).intersection(set(compartment_2))

    # 3: Determine the priority
    letter = next(iter(intersection_dict))
    priority = get_priority(letter)

    # 4: Sum up the results
    total += priority

print(total)