grid_inp = True
instructions = ""
i = 0
obstacles = set()
boxes = set()
dirxns = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
b = 0
print_mode = True

while True:
    try:
        inp = input()
        if len(inp) == 0:
            grid_inp = False
            
        if grid_inp:
            j = 0
            for letter in inp:
                if letter == "#":
                    obstacles.add((i, j))
                    obstacles.add((i, j+1))
                elif letter == "@":
                    robot = (i, j)
                elif letter == "O":
                    boxes.add((i, j))
                j += 2
            b = max(j, b)
            i += 1
        else:
            instructions += inp
    except Exception as e:
        break
l = i
head = """{"version": 2, "width": 100, "height": 50, "timestamp": 1734271647, "env": {"SHELL": "/bin/fish", "TERM": "xterm"}}"""
print(head)
def get_box_vert(i, j, box=True):
    inter = set()
    if box:
        inter = {(i, j), (i, j+1), (i, j-1)}.intersection(boxes)
    else:
        inter = {(i, j), (i, j-1)}.intersection(boxes)
    return inter
def get_obstacle_vert(i, j, box=True):
    inter = set()
    if box:
        inter = {(i, j), (i, j+1)}.intersection(obstacles)
    else:
        inter = {(i, j)}.intersection(obstacles)
    return inter

def get_box_hor(i, j, dirxn):
    inter = set()
    if dirxn == "<":
        inter = {(i, j-1)}.intersection(boxes)
    if dirxn == ">":
        inter = {(i, j)}.intersection(boxes)
    return inter
def get_obstacle_hor(i, j):
    inter = {(i, j)}.intersection(obstacles)
    return inter
def move(box, dirxn):
    i, j = box
    curr_boxes = {(box)}
    di, dj = dirxns[dirxn]
    if dirxn in "<>":
        if dirxn == ">":
            nexboxes = get_box_hor(i+di, j+dj+1, dirxn)
            nexobs = get_obstacle_hor(i+di, j+dj+1)
        if dirxn == "<":
            nexboxes = get_box_hor(i+di, j+dj, dirxn)
            nexobs = get_obstacle_hor(i+di, j+dj)
    else:
        nexboxes = get_box_vert(i+di, j+dj)
        nexobs = get_obstacle_vert(i+di, j+dj)
    if len(nexobs):
        return set()
    if len(nexboxes):
        curr_boxes.update(nexboxes)
        for nexbox in nexboxes:
            nexnexboxes = move(nexbox, dirxn)
            if len(nexnexboxes) == 0:
                return set()
            curr_boxes.update(nexnexboxes)
    return curr_boxes

i, j = robot
ic_count = 0
for instruction in instructions:
    ic_count += 1
    di, dj = dirxns[instruction]
    nexboxes = set()
    bxs = set()
    #print(ic_count - 1, i, j)
    if instruction in "<>":
        if get_box_hor(i+di, j+dj, instruction):
            bxs = get_box_hor(i+di, j+dj, instruction)
        elif get_obstacle_hor(i+di, j+dj):
            continue
    else:
        if get_box_vert(i+di, j+dj, box=False):
            bxs = get_box_vert(i+di, j+dj, box=False)
        elif get_obstacle_vert(i+di, j+dj, box=False):
            continue
    for bx in bxs:
        nexboxes.update(move(bx, instruction))
    if len(nexboxes):
        boxes.difference_update(nexboxes)
        boxes.update({(nexbox[0]+di, nexbox[1]+dj) for nexbox in nexboxes})
        i += di
        j += dj
    elif len(bxs) == 0:
        i += di
        j += dj
    out_string = ""
    if print_mode and ic_count % 10 == 0:
        grid = [["." for j in range(b)] for i in range(l)]
        for box in boxes:
            ci, cj = box
            grid[ci][cj] = "["
            grid[ci][cj+1] = "]"
        for obstacle in obstacles:
            ci, cj = obstacle
            grid[ci][cj] = "#"
        grid[i][j] = "@"
        for row in grid:
            out_string += "".join(row)
            out_string += """\\r\\n"""
        print(f'[{ic_count/len(instructions)*10}, "o", "\\u001b[2J\\r\\u001b[32m"]')
        print(f'[{ic_count/len(instructions)*10}, "o", "{ic_count/len(instructions)*100:.2f}% complete\\r\\n"]')
        print(f'[{ic_count/len(instructions)*10}, "o", "{out_string}"]')
count = 0
for box in boxes:
    count += box[0]*100 + box[1]
