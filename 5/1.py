order = dict()

rules = True
pages = []
while True:
    try:
        inp = input()
        if rules:
            try:
                a, b = (int(i) for i in inp.split("|"))
                if a not in order:
                    order[a] = set()
                order[a].add(b)
            except Exception as e:
                rules = False
                continue
        else:
            pages.append([int(i) for i in inp.split(",")])
    except Exception as e:
        break
def is_before(a, b):
    if a not in order:
        return False
    return b in order[a]
count = 0
for page in pages:
    curr = page[0]
    ordered = True
    for i in page[1:]:
        if not is_before(curr, i):
            ordered = False
            break
        curr = i
    if ordered:
        count += page[len(page)//2]
print(count)
