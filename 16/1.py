import heapq
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


queue = [(0, start[0], start[1], 0, 1)]
visited = dict()
while len(queue):
    dist, i, j, dxi, dxj = heapq.heappop(queue)
    if (i, j) in visited:
        if visited[(i, j)] < dist:
            continue
    visited[(i, j)] = dist
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ci, cj = i+di, j+dj
        if (di, dj) == (-dxi, -dxj):
            continue
        if (di, dj) == (dxi, dxj):
            score = dist + 1
        else:
            score = dist + 1001
        if grid[ci][cj] == ".":
            heapq.heappush(queue, (score, ci, cj, di, dj))
        if grid[ci][cj] == "E":
            count = score
            queue = []
            break
            

print(count)

