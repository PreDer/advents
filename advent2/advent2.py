file = open("input")
points = 0
for line in file:
    opponent = line[0]
    myself = line[2]
    if myself == "X":
        points = points + 1
    elif myself == "Y":
        points = points + 2
    elif myself == "Z":
        points = points + 3

    if (opponent == "A" and myself == "X") or (opponent == "B" and myself == "Y") or (opponent == "C" and myself == "Z"):
        points = points + 3
    elif (opponent == "B" and myself == "X") or (opponent == "C" and myself == "Y") or (opponent == "A" and myself == "Z"):
        points = points + 0
    else:
        points = points + 6

print(points)
