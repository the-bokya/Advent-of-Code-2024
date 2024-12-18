grid = [["." for _ in range(71)] for _ in range(71)]
bs = []
while True:
    try:
        i, j = [int(i) for i in input().split(",")]
        bs.append((i, j))
    except Exception as e:
        break

start = (0, 0)
end  = (70, 70)
found = False
for bdx, b in enumerate(bs):
    grid[b[0]][b[1]] = "#"
    queue = [(0, start)]
    visited = set()
    reached = False
    while queue:
        dist, current = queue.pop(0)
        i, j = current
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ci, cj = i+di, j+dj
            if ci < 0 or ci > 70:
                continue
            if cj < 0 or cj > 70:
                continue
            if (ci, cj) == end:
                reached = True
                queue = []
                break
            if (ci, cj) in visited:
                continue
            if grid[ci][cj] == ".":
                queue.append((dist+1,(ci, cj)))
                visited.add((ci, cj))
    if reached == False:
        print(b)
        break
