grid = []

while True:
    try:
        inp = list(input())
        grid.append(inp)
    except:
        break
og_grid = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
l = len(grid)
b = len(grid[0])
flat = set()
def outside_corner(outsider, visited):
    i, j = outsider
    corners = 0
    for dx, dy in ([-1, -1], [1, -1], [-1, 1], [1, 1]):
        ai, aj = i+dx, j+dy
        bi, bj = i+dx, j
        ci, cj = i, j+dy
        cnt = 0
        for ni, nj in [(ai, aj), (bi, bj), (ci, cj)]:
            if ni < 0 or ni >= l:
                break
            if nj < 0 or nj >= b:
                break
            if (ni, nj) in visited:
                cnt += 1
        if cnt == 3:
            corners += 1
    return corners

def nebinator(nebs):
    nebs = list(nebs)
    if len(nebs) == 4:
        return 0
    if len(nebs) == 3:
        return 0
    if len(nebs) == 2:
        a = nebs[0]
        b = nebs[1]
        vert_distance = abs(a[0] - b[0]) 
        hor_distance = abs(a[1] - b[1])
        if hor_distance == 0 or vert_distance == 0:
            return 0
        return 1
    if len(nebs) == 1:
        return 2
    return 4

def traverse(i, j):
    letter = grid[i][j]
    visited = {(i, j)}
    area = 1
    perimeter = 0
    nexts = [(i, j)]
    corners = 0
    common_outsiders = set()
    while nexts:
        next = nexts.pop(0)
        nebs = set()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            c_i, c_j = next[0] + di, next[1] + dj
            if c_i < 0 or c_i >= l:
                continue
            if c_j < 0 or c_j >= b:
                continue
            if grid[c_i][c_j] == None:
                if (c_i, c_j) not in visited:
                    common_outsiders.add((c_i, c_j))
                else:
                    nebs.add((c_i, c_j))
                continue
            if grid[c_i][c_j] != letter:
                common_outsiders.add((c_i, c_j))
                continue
            if (c_i, c_j) in visited:
                nebs.add((c_i, c_j))
                continue
            visited.add((c_i, c_j))
            area += 1
            nebs.add((c_i, c_j))
            nexts.append((c_i, c_j))
            flat.add((c_i, c_j))
            grid[c_i][c_j] = None
        corners += nebinator(nebs)
    for outsider in common_outsiders:
        corners += outside_corner(outsider, visited)
    return area, corners

count = 0

for i in range(l):
    for j in range(b):
        if (i, j) not in flat:
            area, corners = traverse(i, j)
            count += area*corners
print(count)
