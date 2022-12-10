with open('input.txt') as f:
    lines = f.readlines()

cycles = [1]
i = 1
crt = [["." for x in range(40)] for i in range(6)]
crt[0][0] = "#"

for line in lines:
    command = line.strip().split()

    # part 1 just do work for noop / add phase 1 anyways since they are the same logically
    cycles.append(1)
    cycles[i] = cycles[i - 1]
    i += 1

    if command[0] == "addx":
        cycles.append(1)
        cycles[i] = cycles[i-1] + (int(command[1]))
        i += 1

    # part 2 same for noop / add cycle part 1 then do extra step if addx
    if (i - 1) % 40 in range(cycles[i - 1] - 1, cycles[i - 1] + 2):
        crt[(i - 1) // 40][(i - 1) % 40] = "#"
    if command[0] == "addx":
        if (i - 2) % 40 in range(cycles[i - 2] - 1, cycles[i - 2] + 2):
            crt[(i - 2) // 40][(i - 2) % 40] = "#"

print(sum([cycles[20 - 1] * 20, cycles[60 - 1] * 60, cycles[100 - 1] * 100, cycles[140 - 1] * 140, cycles[180 - 1] * 180, cycles[220 - 1] * 220]))

# draw CRT
for row in crt:
    for col in row:
        print(col, end="")
    print("")
