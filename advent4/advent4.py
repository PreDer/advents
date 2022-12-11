file = open("input")
# file = open("input_test")

ding = 0
for line in file:
    split = line.split(",")
    firstA = split[0]
    secondA = split[1]

    splitFirstA = firstA.split("-")
    firstNumberOfFirst = int(splitFirstA[0])
    secondNumberOfFirst = int(splitFirstA[1])

    splitSecondA = secondA.split("-")
    firstNumberOfSecond = int(splitSecondA[0])
    secondNumberOfSecond = int(splitSecondA[1])

    if (firstNumberOfFirst <= firstNumberOfSecond and secondNumberOfFirst >= secondNumberOfSecond) or \
            (firstNumberOfSecond <= firstNumberOfFirst and secondNumberOfSecond >= secondNumberOfFirst):
        ding = ding + 1

print(ding)
