from threading import Thread

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

def step(i, j, di, dj, visited=None, obstacle=(100000, 100000)):
    if visited != None:
        visited.add((i, j))
    if i == 0 or i == l-1:
        return i, j, di, dj, True
    if j == 0 or j == b-1:
        return i, j, di, dj, True
    for _ in range(2):
        if grid[i+di][j+dj] == "#" or (i+di, j+dj) == obstacle:
            di, dj = turn(di, dj)
    i, j = i+di, j+dj
    return i, j, di, dj, False


while True:
    i, j, di, dj, done = step(i, j, di, dj, visited)
    if done:
        break


obs = set()
iterated = 0
for i, j in visited:
    iterated += 1
    if iterated % 10 == 0:
        print(f"{iterated/len(visited) * 100}% complete")
    ai, aj = start
    bi, bj = start

    adi, adj = (-1, 0)
    bdi, bdj = (-1, 0)
    obstacle = (i, j)
    idx = 0
    if obstacle in obs:
        continue
    while True:
        ai, aj, adi, adj, done = step(ai, aj, adi, adj, obstacle=obstacle)
        if done:
            break
        if idx % 2:
            bi, bj, bdi, bdj, done = step(bi, bj, bdi, bdj, obstacle=obstacle)
        if (ai, aj) == (bi, bj) and (adi, adj) == (bdi, bdj):
            obs.add(obstacle)
            break
        idx += 1

print(len(obs))
