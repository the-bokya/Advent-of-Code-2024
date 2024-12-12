grid = []

while True:
    try:
        inp = list(input())
        grid.append(inp)
    except:
        break
l = len(grid)
b = len(grid[0])
flat = set()
def traverse(i, j):
    letter = grid[i][j]
    visited = {(i, j)}
    area = 1
    perimeter = 0
    nexts = [(i, j)]
    while nexts:
        next = nexts.pop(0)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            c_i, c_j = next[0] + di, next[1] + dj
            if c_i < 0 or c_i >= l:
                perimeter += 1
                continue
            if c_j < 0 or c_j >= b:
                perimeter += 1
                continue
            if grid[c_i][c_j] == None:
                if (c_i, c_j) not in visited:
                    perimeter += 1
                continue
            if grid[c_i][c_j] != letter:
                perimeter += 1
                continue
            if (c_i, c_j) in visited:
                continue
            visited.add((c_i, c_j))
            area += 1
            nexts.append((c_i, c_j))
            flat.add((c_i, c_j))
            grid[c_i][c_j] = None

    return area, perimeter

count = 0

for i in range(l):
    for j in range(b):
        if (i, j) not in flat:
            area, perimeter = traverse(i, j)
            count += area*perimeter
print(count)
