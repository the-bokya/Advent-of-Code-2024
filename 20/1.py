from collections import Counter
grid = []
l = 0
start = (0, 0)
obs = set()
while True:
    try:
        inp = input()
        if "S" in inp:
            start = (l, inp.index("S"))
        if "E" in inp:
            end = (l, inp.index("E"))
        grid.append(inp)
        for ldx, letter in enumerate(inp):
            if letter == "#":
                obs.add((l, ldx))
        l += 1
    except:
        break
l = len(grid)
b = len(grid[0])
def traverse(cheat):
    count = 0
    queue = [(0, start[0], start[1], 0, 1,  tuple())]
    visited = set()
    dists = dict()
    og = float("inf")
    cheats = dict()
    cheat_prev = False
    while len(queue):
        dist, i, j, dxi, dxj, cheat_branch = queue.pop(0)
        if (i, j, cheat_branch) in visited:
            continue
        visited.add((i, j, cheat_branch))
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ci, cj = i+di, j+dj
            if (di, dj) == (-dxi, -dxj):
                continue
            score = dist + 1
            if ci < 0 or ci >= l:
                continue
            if cj < 0 or cj >= b:
                continue
            if grid[ci][cj] == "E":
                dists[cheat_branch] = score
            if grid[ci][cj] == ".":
                if len(cheat_branch) == 1:
                    queue.append((score, ci, cj, di, dj, cheat_branch + ((ci, cj), )))
                else:
                    queue.append((score, ci, cj, di, dj, cheat_branch))
            if (ci, cj) == cheat:
                queue.append((score, ci, cj, di, dj, ((ci, cj), ) ))
    return dists
count = 0
for obdx, ob in enumerate(obs):
    print((obdx * 100)/len(obs))
    dists = traverse(ob)
    og = dists[()]
    for cheat_dist in dists:
        if og - dists[cheat_dist] >= 100:
            count += 1
print(count)
