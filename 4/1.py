grid = []

count = 0


while True:
    try:
        grid.append(input())
    except:
        break
l = len(grid)
b = len(grid[0])

def search(x, y, dx, dy):
    global l, b, grid
    c_x, c_y = x, y
    for letter in "XMAS":
        if not (0 <= c_x < b):
            return False
        if not (0 <= c_y < l):
            return False

        if grid[c_y][c_x] == letter:
            c_x += dx
            c_y += dy
            continue
        return False
    return True
for y, line in enumerate(grid):
    for x, letter in enumerate(line):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if search(x, y, dx, dy):
                    count += 1
print(count)

