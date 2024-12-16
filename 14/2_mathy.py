import re
from functools import reduce
from sys import argv
l = 103
b = 101
robots = []
print_mode = False
if len(argv) > 1:
    if argv[1] == "print":
        print_mode = True

def make_grid(robots, second):
    for robot in robots:
        x, y, vx, vy = robot
        nx, ny = (x + vx * second) % b, (y + vy * second) % l
        grid[ny][nx] = "#"
    return grid

def show_grid(grid):
    for row in grid:
        s = "".join(row)

        print(s)

# solution based on the probability of the robots appearing in a
# square kernel region vs in general
def jadu_factor_finder(robots, l, b):
    num_robots = len(robots)
    probability = num_robots / (l*b)
    kernel_length = 2
    kernel_size = kernel_length**2
    out = 0
    for i in range(l-kernel_length):
        for j in range(b-kernel_length):
            num_robots_in_kernel = 0
            for di in range(kernel_length):
                for dj in range(kernel_length):
                    if (i+di, j+dj) in robots:
                        num_robots_in_kernel += 1
            probability_in_kernel = num_robots_in_kernel / (kernel_size)
            # Squaring the difference creates a noticeable gap between
            # kernels having random occurences of the robots and kernels
            # with too much or too less occurences of robots
            # adding up is comparable to averages as the denominator doesn't
            # change during comparison.
            # When you compare a random image with an image having the ascii art,
            # there's a HUGE difference between them!
            out += (probability - probability_in_kernel)**2
    return out
while True:
    try:
        x, y, vx, vy = [int(i) for i in re.findall("-?[0-9]+", input())]
        robots.append((x, y, vx, vy))
    except Exception as e:
        break

qs = [0, 0, 0, 0]
jadu_factor = 0
jadu_second = 0
for second in range(10000):
    grid = [[" " for j in range(b)] for i in range(l)]
    new_robots = set()
    for robot in robots:
        x, y, vx, vy = robot
        nx, ny = (x + vx * second) % b, (y + vy * second) % l
        new_robots.add((nx, ny))
    c_jadu_factor = jadu_factor_finder(new_robots, l, b)
    if c_jadu_factor > jadu_factor:
        print(second)
        jadu_factor = c_jadu_factor
        jadu_second = second
    if print_mode:
        print("-"*40)
        print(second)
        show_grid(grid)
show_grid(make_grid(robots, jadu_second))
print(jadu_second)
