import re
from functools import reduce
from sys import argv
l = 103
b = 101
robots = []
print_mode = False
if len(argv) > 1:
    if argv[1] == "print":
        print_mode = True
while True:
    try:
        x, y, vx, vy = [int(i) for i in re.findall("-?[0-9]+", input())]
        robots.append((x, y, vx, vy))
    except Exception as e:
        break

qs = [0, 0, 0, 0]
for second in range(10000):
    grid = [[" " for j in range(b)] for i in range(l)]
    for robot in robots:
        x, y, vx, vy = robot
        nx, ny = (x + vx * second) % b, (y + vy * second) % l
        grid[ny][nx] = "#"
    if print_mode:
        print("-"*40)
        print(second)
    for row in grid:
        s = "".join(row)

        # after finding the tree ascii art, it's clear we're looking for many adjacent "#"s
        if "#########" in s:
            print(second)
            break
        if print_mode:
            print(s)
