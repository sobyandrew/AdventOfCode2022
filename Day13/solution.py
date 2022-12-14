import ast
with open('test.txt') as f:
    lines = f.readlines()

i = 0
left =[]
right =[]

while i < len(lines):
    if lines[i].strip() == "":
        i +=1
    else:
        left.append(ast.literal_eval(lines[i].strip()))
        right.append(ast.literal_eval(lines[i+1].strip()))
        i +=2

def comp(a,b):
    items = zip(a,b)
    for x, y in items:
        if isinstance(x, list) and isinstance(y, list):
            val = comp(x,y)
            if abs(val) == 1:
                return val
            # if x < y:
            #     return 1
            # if x > y:
            #     return -1
            # else:
            #     return 0

        elif isinstance(x, list) and isinstance(y, int):
            #convert y to list and resend
            val = comp(x,[y])
            if abs(val) == 1:
                return val

        elif isinstance(x, int) and isinstance(y, list):
            #convert x to list and resend
            val = comp([x],y)
            if abs(val) == 1:
                return val
        else:
            # val = comp(x,y)
            # if abs(val) == 1:
            #     return val
            if x < y:
                return 1
            if x > y:
                return -1
            else:
                return 0


    iflen(a) > len(b)):
        return -1
    elif(len(b) > len(a)):
        return 1
    else:
        return 0
idx = 1
count = 0
runningTotal = 0
for pack1, pack2 in zip(left, right):
    print(pack1)
    print(pack2)
    if comp(pack1,pack2):
        count +=1
        print("here at :", idx)
        runningTotal += idx
    idx+=1

print(runningTotal)
print(count)




