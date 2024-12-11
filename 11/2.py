from collections import Counter
from functools import cache
stones = [int(i) for i in input().split()]

@cache
def stoner(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stonestr = str(stone)
        l = len(stonestr)
        return [int(stonestr[:l//2]), int(stonestr[l//2:])]
    return [stone * 2024]

current = Counter(stones)
for i in range(75):
    new_stones = Counter()
    for stone in current.keys():
        for new_stone in stoner(stone):
            new_stones[new_stone] += current[stone]
    current = new_stones
count = 0
for k in current:
    count += current[k]
print(count)
