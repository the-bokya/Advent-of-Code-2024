import heapq
import os
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
        grid.append(list(inp))
        l += 1
    except:
        break


queue = [(0, start[0], start[1], 0, 1, set())]
visited = dict()
paths = set()
count = float("inf")
while len(queue):
    dist, i, j, dxi, dxj, path = heapq.heappop(queue)
    #print(len(queue))
    if dist > count:
        continue
    if (i, j, dxi, dxj) in visited:
        if (visited[(i, j, dxi, dxj)]) < dist:
            continue
    visited[(i, j, dxi, dxj)] = dist
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ci, cj = i+di, j+dj
        if (di, dj) == (-dxi, -dxj):
            continue
        if (di, dj) == (dxi, dxj):
            score = dist + 1
        else:
            score = dist + 1001
        if grid[ci][cj] == ".":
            heapq.heappush(queue, (score, ci, cj, di, dj, path.union(set([(ci, cj)]))))
        if grid[ci][cj] == "E":
            print("meow", path)
            count = score
            paths.update(path)
            continue
l = len(grid)
b = len(grid[0])
idx = 0
print(paths)
for p in paths:
    print(p)
    grid[p[0]][p[1]] = "B"
for row in grid:
    print(" ".join(row))
print(count, len(paths)+2)
