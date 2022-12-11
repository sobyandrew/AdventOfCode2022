with open('input.txt') as f:
    lines = f.readlines()


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = []
        self.test = 0
        self.t = 0
        self.f = 0
        self.inspectCount = 0

    def monkeyInfo(self):
        print("items:", end="")
        for item in self.items:
            print(item, "", end="")
        print("")
        print("inspected:", self.inspectCount)


i = 0

monkeys = []

while i < len(lines) - 1:
    if lines[i].strip() == "":
        i += 1
        continue

    m = Monkey()

    # get items for monkey
    command = lines[i + 1].strip().replace(",", "").split()
    for x in range(2, len(command)):
        m.items.append(int(command[x]))
        # print(command[x])

    # get command and val to change by
    command = lines[i + 2].strip().split()
    m.operation.append(command[4])
    m.operation.append(command[5])

    command = lines[i + 3].strip().split()
    m.test = int(command[-1])

    command = lines[i + 4].strip().split()
    m.t = int(command[-1])

    command = lines[i + 5].strip().split()
    m.f = int(command[-1])

    monkeys.append(m)
    i += 6


commonMod = 1
for m in monkeys:
    commonMod *= m.test

for y in range(0, 10000):
    for monkey in monkeys:
        for item in monkey.items:
            if monkey.operation[0] == "+":
                if monkey.operation[1] == "old":
                    item *= 2
                else:
                    item += int(monkey.operation[1])
            else:
                if monkey.operation[1] == "old":
                    val = item
                    item *= val
                else:
                    item *= int(monkey.operation[1])

            item = item % commonMod
            monkey.inspectCount += 1
            # check if value is divisible and is true
            if item % monkey.test == 0:
                monkeys[monkey.t].items.append(item)
            else:
                monkeys[monkey.f].items.append(item)

        monkey.items.clear()

m1 = max(monkeys[0].inspectCount, monkeys[1].inspectCount)
m2 = min(monkeys[0].inspectCount, monkeys[1].inspectCount)
for index in range(2, len(monkeys)):
    if monkeys[index].inspectCount > m1:
        m2 = m1
        m1 = monkeys[index].inspectCount
    elif monkeys[index].inspectCount > m2:
        m2 = monkeys[index].inspectCount

print(m1 * m2)
