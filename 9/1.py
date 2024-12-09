import heapq
nums = [int(i) for i in input()]

i = 0
idx = 0
disk = []
empties = []
while True:
    try:
        file = nums.pop(0)
        disk.extend([i]*file)
        idx += file
        block = nums.pop(0)
        empties.extend([j for j in range(idx, idx + block)])
        idx += block
        disk.extend([None]*block)
        i += 1
    except Exception as e:
        break
heapq.heapify(empties)
rdx = len(disk) - 1
while rdx >= 0 and empties:
    curr = disk[rdx]
    if curr == None or empties[0] > rdx:
        rdx -= 1
        continue
    disk[rdx] = None
    empty = heapq.heappop(empties)
    heapq.heappush(empties, rdx)
    disk[empty] = curr
    rdx -= 1

count = 0

for idx, i in enumerate(disk):
    if i == None:
        break
    count += idx * i
print(count)
