from collections import Counter
from sys import setrecursionlimit

setrecursionlimit(140*140)
grid = []
l = 0
start = (0, 0)
while True:
    try:
        inp = input()
        if "S" in inp:
            start = (l, inp.index("S"))
        if "E" in inp:
            end = (l, inp.index("E"))
        grid.append(inp)
        l += 1
    except:
        break
l = len(grid)
b = len(grid[0])
dists = dict()
def traverse(strt, dxi, dxj):
    count = 0
    i, j = strt
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ci, cj = i+di, j+dj
        if (di, dj) == (-dxi, -dxj):
            continue
        if ci < 0 or ci >= l:
            continue
        if cj < 0 or cj >= b:
            continue
        if grid[ci][cj] == "E":
            dist = 1
            dists[strt] = dist
            return 1
        if grid[ci][cj] == ".":
            dist = 1 + traverse((ci, cj), di, dj)
            dists[strt] = dist
            return dist

traverse(start, -1, -1)
dists[end] = 0
count = 0
for coord in dists:
    i, j = coord
    for x in range(-20, 21):
        for y in range(-20, 21):
            manhattan = abs(x) + abs(y)
            if manhattan > 20:
                continue
            cheat = (i + y, j + x)
            if cheat in dists:
                new_dist = dists[cheat] + manhattan
                saved = dists[coord] - new_dist
                if saved >= 100:
                    count += 1
print(count)
