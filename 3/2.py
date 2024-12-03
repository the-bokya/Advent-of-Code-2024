import re
inp = ""
while True:
    try:
        inp += input()
    except:
        break

grps = re.findall(r"mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don\'t\(\))", inp)
count = 0
enabled = True
for a, b, do, dont in grps:
    if do:
        enabled = True
    elif dont:
        enabled = False
    else:
        if enabled:
            count += int(a) * int(b)
print(count)



