import re
antennas = dict()
grid = []
i = 0
while True:
    try:
        inp = input()
        for s in re.finditer("[0-9a-zA-Z]", inp):
            antenna = s.group()
            j = s.span()[0]
            if antenna not in antennas:
                antennas[antenna] = []
            antennas[antenna].append((i, j))
        grid.append(inp)
        i += 1
    except Exception as e:
        break

l = len(grid)
b = len(grid[0])

antinodes = set()
in_bounds = lambda t: 0 <= t[0] < l and 0 <= t[1] < b
for antenna in antennas:
    for adx, ap in enumerate(antennas[antenna]):
        for bdx, bp in enumerate(antennas[antenna][adx+1:]):
            ai, aj = ap
            bi, bj = bp
            di, dj = (bi - ai, bj - aj)
            ci, cj = (ai, aj)
            while in_bounds((ci, cj)):
                antinodes.add((ci, cj))
                ci, cj = ci - di, cj - dj
            ci, cj = (bi, bj)
            while in_bounds((ci, cj)):
                antinodes.add((ci, cj))
                ci, cj = ci + di, cj + dj
print(len(antinodes))
