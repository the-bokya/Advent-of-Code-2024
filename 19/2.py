from functools import cache
available_towels = input().split(", ")
input()
patterns = []
while True:
    try:
        patterns.append(input())
    except:
        break
print(patterns)

@cache
def traverse(s):
    if len(s) == 0:
        return 1
    ways = 0
    for towel in available_towels:
        if s.startswith(towel):
            ways += traverse(s[len(towel):])
    return ways
count = 0
for pattern in patterns:
    count += traverse(pattern)
print(count)
