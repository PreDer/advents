file = open("input")

# a-z  1  - 26  -> 97 - 122 | -96
# A-Z  27 - 52  -> 65 - 90  | -38

sums = 0
for line in file:
    lineLength = int
    lineLength = len(line) // 2
    firstCom = line[:lineLength]
    secondCom = line[lineLength:]

    for element in firstCom:
        if element in secondCom:
            value = ord(element)
            if value < 91:
                print(chr((value)))
                print(value - 38)
                sums = sums + (value - 38)
            else:
                print(chr((value)))
                print(value - 96)
                sums = sums + (value - 96)
            break

print("sum of the priorities:", sums)
