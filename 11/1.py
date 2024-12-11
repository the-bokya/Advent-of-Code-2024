stones = [int(i) for i in input().split()]

def stoner(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stonestr = str(stone)
        l = len(stonestr)
        return [int(stonestr[:l//2]), int(stonestr[l//2:])]
    return [stone * 2024]

current = stones.copy()
for i in range(25):
    new_stones = []
    for stone in current:
        new_stones.extend(stoner(stone))
    current = new_stones

print(len(current))
