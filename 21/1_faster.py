from functools import cache
import re
args = []
for _ in range(5):
    args.append(input())

num_keypad = ["789", "456", "123", "-0A"]
dir_keypad = ["-^A", "<v>"]

num_map = dict()
dir_map = dict()
for idx, i in enumerate(num_keypad):
    for jdx, j in enumerate(i):
        num_map[j] = (idx, jdx)

for idx, i in enumerate(dir_keypad):
    for jdx, j in enumerate(i):
        dir_map[j] = (idx, jdx)

print(dir_map)
@cache
def dir_dir_move(a, b):
    si, sj = a
    ei, ej = b
    di, dj = ei - si, ej - sj
    queue = [("", a)]
    outs = []
    if ei > si:
        di = 1
        v = "v"
    elif ei == si:
        di = 0
    else:
        di = -1
        v = "^"

    if ej > sj:
        dj = 1
        h = ">"
    elif ej == sj:
        dj = 0
    else:
        dj = -1
        h = "<"
    while queue:
        output, cs = queue.pop(0)
        ci, cj = cs
        
        if (ci, cj) == b:
            outs.append(output)
            continue
        if dir_keypad[ci][cj] == "-":
            continue
        if ei != ci:
            queue.append((output+v, (ci+di, cj)))
        if ej != cj:
            queue.append((output+h, (ci, cj+dj)))
    return outs

@cache
def num_dir_move(a, b):
    si, sj = a
    ei, ej = b
    di, dj = ei - si, ej - sj
    queue = [("", a)]
    outs = []
    if ei > si:
        di = 1
        v = "v"
    elif ei == si:
        di = 0
    else:
        di = -1
        v = "^"

    if ej > sj:
        dj = 1
        h = ">"
    elif ej == sj:
        dj = 0
    else:
        dj = -1
        h = "<"
    while queue:
        output, cs = queue.pop(0)
        ci, cj = cs
        
        if (ci, cj) == b:
            outs.append(output)
            continue
        if num_keypad[ci][cj] == "-":
            continue
        if ei != ci:
            queue.append((output+v, (ci+di, cj)))
        if ej != cj:
            queue.append((output+h, (ci, cj+dj)))
    return outs

def num_to_dir(nums):
    current = num_map["A"]
    output = [""]
    for num in nums:
        next = num_map[num]
        next_moves = num_dir_move(current, next)
        new_output = []
        for out in output:
            for next_move in next_moves:
                new_output.append(out+next_move+"A")
        output = new_output
        current = next
    return tuple(output)

@cache
def minimise(ls, n=25):
    if n == 0:
        return min(ls, key=len)
    outs = []
    for ldx, l in enumerate(ls):
        out = ""
        current = "A"
        for letter in l:
            out += minimise(tuple(dir_dir_move(dir_map[current], dir_map[letter])), n-1)
            out += "A"
            current = letter
        out += minimise(tuple(dir_dir_move(dir_map[current], dir_map["A"])), n-1)
        outs.append(out)
    return min(outs, key=len)
count = 0
print(count, args)
for arg in args:
    print(count, arg)
    x = minimise(num_to_dir(arg), n=2)
    #print(x)
    count += len(x) * int(re.findall("[0-9]+", arg)[0])
print(count)
