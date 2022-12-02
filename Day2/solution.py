with open('input.txt') as f:
    lines = f.readlines()

playScores = {'X': 1, 'Y': 2, 'Z': 3}

# a -> rock b -> paper c-> scissors
# x -> rock y -> paper z > scissors
# rock -> 1 paper -> 2 scissors -> 3

totalScore = 0

for line in lines:
    currRound = line.strip().replace(" ", "")
    a, b = currRound[0], currRound[1]
    totalScore += playScores[b]

    # determine win or tie or loss
    if (b == 'Z' and a == 'B') or (b == 'Y' and a == 'A') or (b == 'X' and a == 'C'):
        totalScore += 6
    elif ord(b) - ord(a) == 23:
        totalScore += 3

print(totalScore)

# part 2
# a -> rock b -> paper c-> scissors
# x -> lose y -> draw z -> win
# rock -> 1 paper -> 2 scissors -> 3

lose = {'A': 3, 'B': 1, 'C': 2}
win = {'A': 8, 'B': 9, 'C': 7}
draw = {'A': 4, 'B': 5, 'C': 6}

totalScore = 0

for line in lines:
    currRound = line.strip().replace(" ", "")
    a, b = currRound[0], currRound[1]

    if b == 'X':
        totalScore += lose[a]
    elif b == 'Y':
        totalScore += draw[a]
    else:
        totalScore += win[a]

print(totalScore)
