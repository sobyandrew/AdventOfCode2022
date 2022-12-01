#day 1 solution 1

with open('input.txt') as f:
    lines = f.readlines()

elfTotals = []
currElf = 0

for line in lines:
    if line.strip() == "":
        elfTotals.append(currElf)
        currElf = 0
    else:
        currElf += int(line.strip())
elfTotals.append(currElf)
print(max(elfTotals))

#solution 2
top3 = 0

for i in range(0,3):
    currMax = max(elfTotals)
    top3 += currMax
    elfTotals.remove(currMax)

print(top3)

