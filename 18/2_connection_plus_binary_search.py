grid = [["." for _ in range(71)] for _ in range(71)]
bs = []
while True:
    try:
        i, j = [int(i) for i in input().split(",")]
        bs.append((i, j))
    except Exception as e:
        break

start = (0, 0)
end  = (70, 70)
found = False

bsd = {i: idx for idx, i in enumerate(bs)}
def traverse(n):
    b = bs[n]
    queue = [b]
    visited = set()
    edge1 = False
    edge2 = False
    while queue:
        current = queue.pop(0)
        i, j = current
        if i == 0 or j == 70:
            edge1 = True
        if i == 70 or j == 0:
            edge2 = True
        if edge1 and edge2:
            return b
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ci, cj = i+di, j+dj
                if ci < 0 or ci > 70:
                    continue
                if cj < 0 or cj > 70:
                    continue
                if (ci, cj) in visited:
                    continue
                if (ci, cj) in bsd:
                    if bsd[(ci, cj)] <= n:
                        queue.append((ci, cj))
                        visited.add((ci, cj))
    return False
l = 0
h = len(bs)

while l <= h:
    if l == h:
        print(traverse(l))
        break
    m = (l+h)//2
    r = traverse(m)
    if r:
        h = m - 1
    else:
        l = m + 1
