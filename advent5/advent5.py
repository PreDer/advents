one = ["H", "C", "R"]
two = ["B", "J", "H", "L", "S", "F"]
three = ["R", "M", "D", "H", "J", "T", "Q"]
four = ["S", "G", "R", "H", "Z", "B", "J"]
five = ["R", "P", "F", "Z", "T", "D", "C", "B"]
six = ["T", "H", "C", "G"]
seven = ["S", "N", "V", "Z", "B", "P", "W", "L"]
eight = ["R", "J", "Q", "G", "C"]
nine = ["L", "D", "T", "R", "H", "P", "F", "S"]

index = [one, two, three, four, five, six, seven, eight, nine]

file = open("input")


def move(amount: int, source: int, target: int):
    for i in range(0, amount):
        x = index[source - 1].pop()
        index[target - 1].append(x)


for line in file:
    split = line.split(" ")
    move(int(split[1]), int(split[3]), int(split[5]))
print(one.pop())
print(two.pop())
print(three.pop())
print(four.pop())
print(five.pop())
print(six.pop())
print(seven.pop())
print(eight.pop())
print(nine.pop())
