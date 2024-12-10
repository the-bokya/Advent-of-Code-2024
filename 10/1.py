grid = []
nums = dict()
i = 0

while True:
    try:
        inp = [int(i) for i in input()]
        b = len(inp)
        grid.append(inp)
        for j, n in enumerate(inp):
            if n not in nums:
                nums[n] = set()

            nums[n].add((i, j))
        i += 1
    except:
        break
l = len(grid)
b = len(grid[0])
pool = dict()
for i, j in nums[0]:
    pool[(i, j)] = {(i, j)}
for level in range(1, 10):
    print(level)
    for (i, j) in nums[level]:
        print(i, j)
        for di, dj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            c_i, c_j = i - di, j - dj
            if c_i < 0 or c_i >= l:
                continue
            if c_j < 0 or c_j >= b:
                continue
            if grid[c_i][c_j] == level - 1:
                if (i, j) not in pool:
                    pool[(i, j)] = set()
                if (c_i, c_j) in pool:
                    pool[(i, j)] = pool[(i, j)].union(pool[(c_i, c_j)])
count = 0
for i, j in nums[9]:
    count += len(pool[(i, j)])
print(count)
