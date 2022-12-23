with open('./input.txt') as f:
	max_calories = 0
	calorie_counter = 0

	for line in f:
		if line.strip():
			calorie_counter += int(line.strip())
		else:
			if calorie_counter > max_calories:
				max_calories = calorie_counter
			calorie_counter = 0

	print(max_calories)
