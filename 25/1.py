locks = []
keys = []

while True:
    try:
        levels = [-1 for _ in range(5)]
        for _ in range(7):
            inp = input()
            for idx, h in enumerate(inp):
                if h == "#":
                    levels[idx] += 1
        if inp == "#####":
            keys.append(levels)
        else:
            locks.append(levels)
        input()
    except:
        break
count = 0
for lock in locks:
    for key in keys:
        fit = True
        for idx in range(5):
            if lock[idx] + key[idx] > 5:
                fit = False
                break
        if fit:
            count += 1
print(count)
