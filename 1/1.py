a, b = [], []

# Assuming you pipe the input. Didn't bother with file handling.
while True:
    try:
        x, y = [int(i) for i in input().split()]
        a.append(x)
        b.append(y)
    except:
        break
a.sort()
b.sort()
count = 0
for x, y in zip(a, b):
    count += abs(x - y)
print(count)
