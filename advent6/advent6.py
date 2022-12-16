file = open("input")
beginning: int
combination = list()
index: int = 0

for line in file:
    for character in line:
        index += 1
        combination.append(character)

        if len(combination) == 5:
            combination.pop(0)

        if (len(combination) == 4) & (len(combination) == len(set(combination))):
            print(index)
            raise SystemExit(0)
