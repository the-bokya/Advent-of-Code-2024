from functools import cmp_to_key
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
def is_cmp_before(a, b):
    if a not in order:
        return 1
    if b in order[a]:
        return -1
    return 0

def is_not_before(a, b):
    return not is_before(a, b)
count = 0
for page in pages:
    curr = page[0]
    ordered = True
    for i in page[1:]:
        if not is_before(curr, i):
            ordered = False
            break
        curr = i
    if not ordered:
        print(page)
        page = sorted(page, key=cmp_to_key(is_cmp_before))
        print(page)
        count += page[len(page)//2]
print(count)
