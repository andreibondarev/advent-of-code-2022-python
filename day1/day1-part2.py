with open('./input.txt') as f:
	calorie_counter = 0
	index = 1
	elf_calories = {}

	for line in f:
		if line.strip():
			if elf_calories.get("elf-" + str(index)):
				elf_calories["elf-" + str(index)] += int(line.strip())
			else:
				elf_calories["elf-" + str(index)] = int(line.strip())
		else:			
			index += 1

values = [v for k,v in elf_calories.items()]
print(sum(sorted(values)[-3:]))