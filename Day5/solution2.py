from collections import deque

with open('input.txt') as f:
    lines = f.readlines()

puzzle = []
s1, s2, s3, s4, s5, s6, s7, s8, s9 = deque(), deque(), deque(), deque(), deque(), deque(), deque(), deque(), deque()
puzzle.extend((s1, s2, s3, s4, s5, s6, s7, s8, s9))
moveFlag = False
print(puzzle)

for line in lines:
    if not moveFlag:
        if line.strip() == "":
            moveFlag = True
        else:
            for i in range(len(line)):
                if line[i] == '[':
                    puzzle[i//4].appendleft(line[i+1])
    else:
        move = line.strip().split(" ")
        boxes = []
        for i in range(int(move[1])):
            boxes.append(puzzle[int(move[3]) - 1].pop())

        boxes.reverse()
        puzzle[int(move[5]) - 1].extend(boxes)

print(puzzle)
for x in puzzle:
    print(x.pop(), end="")



