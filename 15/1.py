grid = []
grid_inp = True
instructions = ""
i = 0
robot = (0, 0)
while True:
    try:
        inp = input()
        if len(inp) == 0:
            grid_inp = False
            
        if grid_inp:
            if "@" in inp:
                robot = (i, inp.index("@"))
            grid.append(list(inp))
            i += 1
        else:
            instructions += inp
    except:
        break


def move(i, j, di, dj):
    if grid[i+di][j+dj] == ".":
        grid[i+di][j+dj] = grid[i][j]
        grid[i][j] = "."
        return True
    if grid[i+di][j+dj] == "#":
        return False
    if grid[i+di][j+dj] == "O":
        if move(i+di, j+dj, di, dj):
            grid[i+di][j+dj] = grid[i][j]
            grid[i][j] = "."
            return True
    return False
dirxns = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
i, j = robot
for instruction in instructions:
    di, dj = dirxns[instruction]
    if move(i, j, di, dj):
        i += di
        j += dj
count = 0
for idx, row in enumerate(grid):
    for jdx, letter in enumerate(row):
        if letter == "O":
            count += idx * 100 + jdx
print(count)

