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
            a_anti = (ai-di, aj-dj)
            b_anti = (bi+di, bj+dj)
            for anti in [a_anti, b_anti]:
                if in_bounds(anti):
                    antinodes.add(anti)
print(len(antinodes))
