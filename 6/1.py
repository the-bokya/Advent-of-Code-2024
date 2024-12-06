grid = []
i = 0
j = -1

while True:
    try:
        inp = input()
        grid.append(inp)
        try:
            j = inp.index("^")
            start = (i, j)
        except:
            pass
        i += 1
    except:
        break

l, b = len(grid), len(grid[0])
i, j = start
di, dj = (-1, 0)
def turn(dx, dy):
    if dx:
        return (-dy, -dx)
    return (dy, dx)
visited = set()
while True:
    visited.add((i, j))
    if i == 0 or i == l-1:
        break
    if j == 0 or j == b-1:
        break
    if grid[i+di][j+dj] == "#":
        di, dj = turn(di, dj)
    i, j = i+di, j+dj

print(len(visited))
