with open('input.txt') as f:
    lines = f.readlines()

commonItems = []

for line in lines:

    sackSize = len(line.strip())
    half = sackSize // 2

    compOne, compTwo = set(), set()

    for i in range(sackSize):
        currItem = line.strip()[i]
        if i < half:
            compOne.add(currItem)
        else:
            if currItem in compOne and currItem not in compTwo:
                commonItems.append(currItem)
            compTwo.add(currItem)

total = 0
for item in commonItems:
    if item.isupper():
        total += ord(item) - 38
    else:
        total += ord(item) - 96

print(total)



