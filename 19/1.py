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
        return True
    for towel in available_towels:
        if s.startswith(towel):
            if traverse(s[len(towel):]):
                return True
    return False
count = 0
for pattern in patterns:
    count += bool(traverse(pattern))
print(count)
