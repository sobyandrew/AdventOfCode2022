with open('input.txt') as f:
    lines = f.readlines()

numPairs = 0
for line in lines:

    intervals = line.strip().split(',')
    elfA, elfB = intervals[0], intervals[1]
    aStart, aEnd = int(elfA.split("-")[0]), int(elfA.split("-")[1])
    bStart, bEnd = int(elfB.split("-")[0]), int(elfB.split("-")[1])

    if (aStart <= bStart and aEnd >= bEnd) or (bStart <= aStart and bEnd >= aEnd):
        numPairs += 1

print(numPairs)

# solution 2
numPairs = 0

for line in lines:

    intervals = line.strip().split(',')
    elfA, elfB = intervals[0], intervals[1]
    aStart, aEnd = int(elfA.split("-")[0]), int(elfA.split("-")[1])
    bStart, bEnd = int(elfB.split("-")[0]), int(elfB.split("-")[1])

    setA = set(range(aStart, aEnd + 1))
    setB = set(range(bStart, bEnd + 1))

    if (setA.intersection(setB) != set()):
        numPairs += 1

print(numPairs)
