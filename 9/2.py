import bisect
nums = [int(i) for i in input()]

i = 0
idx = 0
disk = dict()
empties = []

while True:
    try:
        file = nums.pop(0)
        disk[i] = (idx, file)
        idx += file
        block = nums.pop(0)
        empties.append((idx, block))
        idx += block
        i += 1
    except Exception as e:
        break

for rdx in range(i, -1, -1):
    idx, length = disk[rdx]
    for jdx, empty in enumerate(empties):
        pos, size = empty
        if pos > idx:
            break
        if size >= length:
            empties[jdx] = (pos + length, size - length)
            disk[rdx] = (pos, length)
            break
range_sum = lambda x, y: (y * (y + 1)) // 2 - (x * (x - 1)) // 2
count = 0
for idx in disk:
    pos, length = disk[idx]
    count += range_sum(pos, pos + length - 1) * idx
print(count)
