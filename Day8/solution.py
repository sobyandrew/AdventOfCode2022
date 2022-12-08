with open('input.txt') as f:
    lines = f.readlines()
grid = []
scenicScores = []
for line in lines:
    row = []
    scores = []
    for num in line.strip():
        row.append(int(num))
        scores.append(0)

    grid.append(row)
    scenicScores.append(scores)
edgeTrees = (len(grid) * 2 - 4) + (len(grid[0])) + len(grid[-1])
s = set()

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):

        # check edges + 1 / -1 row + 1 / -1 col
        currTree = grid[i][j]
        holdI = i - 1
        holdJ = j - 1

        # up
        while holdI >= 0:
            nextTree = grid[holdI][j]
            if currTree > nextTree:
                s.add((i, j, "up"))
            else:
                if (i, j, "up") in s:
                    s.remove((i, j, "up"))
                break

            holdI -= 1

        # left
        while holdJ >= 0:
            nextTree = grid[i][holdJ]
            if currTree > nextTree:
                s.add((i, j, "left"))
            else:
                if (i, j, "left") in s:
                    s.remove((i, j, "left"))
                break

            holdJ -= 1

        holdI = i + 1
        holdJ = j + 1

        # down
        while holdI < len(grid):
            nextTree = grid[holdI][j]
            if currTree > nextTree:
                s.add((i, j, "down"))
            else:
                if (i, j, "down") in s:
                    s.remove((i, j, "down"))
                break

            holdI += 1

        # right
        while holdJ < len(grid[i]):
            nextTree = grid[i][holdJ]
            if currTree > nextTree:
                s.add((i, j, "right"))
            else:
                if (i, j, "right") in s:
                    s.remove((i, j, "right"))
                break

            holdJ += 1

uniques = set()

for x, y, z in s:
    if (x, y) not in uniques:
        uniques.add((x, y))

print(edgeTrees + len(uniques))

m = 0

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        k = j
        dLeft = 0
        while k >= 0:
            if k == j:
                k -= 1
            else:
                dLeft += 1
                if grid[i][k] >= grid[i][j]:
                    break
                k -= 1
        k = j
        dRight = 0
        while k < len(grid[i]):
            if k == j:
                k += 1
            else:
                dRight += 1
                if grid[i][k] >= grid[i][j]:
                    break
                k += 1

        k = i
        dUp = 0
        while k >= 0:
            if k == i:
                k -= 1
            else:
                dUp += 1
                if grid[k][j] >= grid[i][j]:
                    break
                k -= 1
        k = i
        dDown = 0
        while k < len(grid):
            if k == i:
                k += 1
            else:
                dDown += 1
                if grid[k][j] >= grid[i][j]:
                    break
                k += 1

        m = max(m, dLeft * dRight * dUp * dDown)

print(m)
#
