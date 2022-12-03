with open('input2.txt') as f:
    lines = f.readlines()

commonItems = []

for i in range(0, len(lines), 3):
    sack1, sack2, sack3 = set(), set(), set()

    line1, line2, line3 = lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip()

    for c in line1:
        sack1.add(c)
    for c in line2:
        sack2.add(c)

    for c in line3:
        if c in sack1 and c in sack2 and c not in sack3:
            commonItems.append(c)
        sack3.add(c)

total = 0
for item in commonItems:
    if item.isupper():
        total += ord(item) - 38
    else:
        total += ord(item) - 96

print(total)
