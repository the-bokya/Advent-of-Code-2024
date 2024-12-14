import re
from functools import reduce
l = 103
b = 101
robots = []
while True:
    try:
        x, y, vx, vy = [int(i) for i in re.findall("-?[0-9]+", input())]
        robots.append((x, y, vx, vy))
    except Exception as e:
        break

qs = [0, 0, 0, 0]

for robot in robots:
    x, y, vx, vy = robot
    nx, ny = (x + vx * 100) % b, (y + vy * 100) % l
    if nx < b // 2:
        if ny < l // 2:
            qs[0] += 1
        elif ny > l // 2:
            qs[2] += 1
    elif nx > b // 2:
        if ny < l // 2:
            qs[1] += 1
        elif ny > l // 2:
            qs[3] += 1
    print(nx, ny)
print(reduce(lambda x, y: x * y, qs))
