from collections import Counter
a, b = [], []

# Assuming you pipe the input. Didn't bother with file handling.
while True:
    try:
        x, y = [int(i) for i in input().split()]
        a.append(x)
        b.append(y)
    except:
        break

a_c, b_c = Counter(a), Counter(b)

count = 0

for x in a_c:
    count += x * a_c[x] * b_c[x]
print(count)
