import re
tokens = 0
lines = []
while True:
    try:
        a1, a2 = [int(i) for i in re.findall("[0-9]+", input())]
        b1, b2 = [int(i) for i in re.findall("[0-9]+", input())]
        c1, c2 = [int(i) for i in re.findall("[0-9]+", input())]
        lines.append((a1, a2, b1, b2, c1, c2))
        input()

    except Exception as e:
        break

for line in lines:
    a1, a2, b1, b2, c1, c2 = line
    c1 += 10000000000000
    c2 += 10000000000000
    x = (b2*c1 - b1*c2) // (b2*a1 - b1*a2)
    y = (a2*c1 - a1*c2) // (a2*b1 - a1*b2)
    if (a1 * x + b1 * y == c1) and (a2 * x + b2 * y == c2):
        tokens += 3*x + y
print(tokens)
