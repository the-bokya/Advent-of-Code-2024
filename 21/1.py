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
def dir_to_dir(dirs):
    current = dir_map["A"]
    output = [""]
    for dir in dirs:
        next = dir_map[dir]
        next_moves = dir_dir_move(current, next)
        new_output = []
        for out in output:
            for next_move in next_moves:
                new_output.append(out+next_move+"A")
        output = new_output
        current = next
    return output
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
    return output

count = 0
for arg in args:
    l1 = num_to_dir(arg)
    l2 = []
    for l in l1:
        l2.extend(dir_to_dir(l))
    l3 = []
    for l in l2:
        l3.extend(dir_to_dir(l))
    count += min([len(i) for i in l3]) * int(re.findall("[0-9]+", arg)[0])
print(count)
