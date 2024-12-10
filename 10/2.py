from collections import Counter
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
zeros = nums[0]
count = 0
for zero in zeros:
    counts = Counter()
    for i, j in nums[0]:
        counts[(i, j)] = 1
for level in range(1, 10):
    for (i, j) in nums[level]:
        for di, dj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            c_i, c_j = i - di, j - dj
            if c_i < 0 or c_i >= l:
                continue
            if c_j < 0 or c_j >= b:
                continue
            if grid[c_i][c_j] == level - 1:
                counts[(i, j)] += counts[(c_i, c_j)]
for i, j in nums[9]:
    count += counts[(i, j)]
print(count)
