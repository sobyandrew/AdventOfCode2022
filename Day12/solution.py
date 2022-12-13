from collections import deque

with open('input.txt') as f:
    lines = f.readlines()

grid = []

for line in lines:
    row = []
    for c in line.strip():
        row.append(c)
    grid.append(row)


def bfs(grid, init):
    q = deque()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in init:
                q.append((i, j, 0, 'a'))

    visited = set()

    for i, j, x, y in q:
        visited.add((i, j))

    def push(i, j, d, a):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[i]): return
        if (i, j) in visited: return
        b = grid[i][j].replace('E', 'z')
        if ord(b) > ord(a) + 1: return
        visited.add((i, j))
        q.append((i, j, d + 1, b))

    while len(q):
        i, j, d, a = q.popleft()
        if grid[i][j] == 'E': return d
        push(i + 1, j, d, a)
        push(i - 1, j, d, a)
        push(i, j + 1, d, a)
        push(i, j - 1, d, a)


init = set()
init.add('S')
init.add('a')
print(init)
print(bfs(grid, init))
