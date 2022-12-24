with open('./input.txt') as f:
  for line in f:
    string = line.strip()

    for i in range(len(string)):
      # Take a 4-char slice of the string
      str = string[i-1:i+3]

      # if sequence marker is found
      if len(set(str)) == 4:
        print(i + 3)
        break

        