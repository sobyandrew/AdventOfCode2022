with open('input.txt') as f:
    lines = f.readlines()

puzzleSize = 4
index = 0
for line in lines:
    s = set()
    for i in range(len(line.strip()) - puzzleSize + 1):
        for x in range(puzzleSize):
            s.add(line[i+x])

        if len(s) < puzzleSize:
            print("too small reset")
            s.clear()
        else:
            print("large enough")
            index = i + puzzleSize
            break

print(index)
print("done")
