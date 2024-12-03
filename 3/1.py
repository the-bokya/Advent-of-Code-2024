import re
inp = ""
while True:
    try:
        inp += input()
    except:
        break

grps = re.findall(r"mul\(([0-9]+),([0-9]+)\)", inp)
count = 0
for a, b in grps:
    count += int(a) * int(b)
print(count)

