with open('input.txt') as f:
    lines = f.readlines()

cycles = []
cycles.append(1)
i = 1

crt = []

for x in range(6):
    row = []
    for j in range(40):
        row.append(".")
    crt.append(row)

for line in lines:
    command = line.strip().split()

    if command[0] == "noop":
        cycles.append(1)
        cycles[i] = cycles[i - 1]
        i += 1

    elif command[0] == "addx":
        cycles.append(1)
        cycles.append(1)
        if i == 0:
            cycles[i] = 1
            cycles[i + 1] = 1 + int(command[1])
            i += 2
        else:
            cycles[i] = cycles[i - 1]
            cycles[i + 1] = cycles[i] + (int(command[1]))
            i += 2

    if command[0] == "noop":
        if (i - 1) % 40 in range(cycles[i - 1] - 1, cycles[i - 1] + 2):
            crt[i // 40][i % 40 - 1] = "#"
    elif command[0] == "addx":
        if (i - 2) % 40 in range(cycles[i - 2] - 1, cycles[i - 2] + 2):
            crt[i // 40][i % 40 - 2] = "#"
        if (i - 1) % 40 in range(cycles[i - 1] - 1, cycles[i - 1] + 2):
            crt[i // 40][i % 40 - 1] = "#"

x = 1
for cycle in cycles:
    print(x, ": ", cycle)
    x += 1

print(len(cycles))
print(
    sum([cycles[20 - 1] * 20, cycles[60 - 1] * 60, cycles[100 - 1] * 100, cycles[140 - 1] * 140, cycles[180 - 1] * 180,
         cycles[220 - 1] * 220]))

# draw CRT
for row in crt:
    for col in row:
        print(col, end="")
    print("")
