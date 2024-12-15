import math
import re
from itertools import batched
from collections import defaultdict
from curses import wrapper
import curses
import time

SIZE_X, SIZE_Y = 101, 103
STEPS = 100


def read_input(filename="input.txt"):
    with open(filename) as f:
        return list(batched([int(d) for d in re.findall(r"-?\d+", f.read())], 4))


def display(stdscr, robot_positions, t, size_x=SIZE_X, size_y=SIZE_Y):
    stdscr.clear()
    for i in range(size_y):
        stdscr.addstr(
            i,
            0,
            "".join(
                [
                    str(robot_positions[(i, j)]) if robot_positions[(i, j)] > 0 else "."
                    for j in range(size_x)
                ]
            ),
        )
    stdscr.addstr(size_y + 1, 0, f"t = {t}")
    stdscr.refresh()


def get_positions(robots):
    robot_positions = defaultdict(int)
    for x, y, _, _ in robots:
        robot_positions[(y, x)] += 1
    return robot_positions


def simulate(robots, size_x=SIZE_X, size_y=SIZE_Y, steps=STEPS):
    quadrant_bounds = [
        (0, size_x // 2, 0, size_y // 2),  # top left
        (size_x // 2 + 1, size_x, 0, size_y // 2),  # top right
        (0, size_x // 2, size_y // 2 + 1, size_y),  # bottom left
        (size_x // 2 + 1, size_x, size_y // 2 + 1, size_y),  # bottom right
    ]
    quadrants = {i: 0 for i in range(len(quadrant_bounds))}
    for i, (x, y, dx, dy) in enumerate(robots):
        x, y = (x + dx * steps) % size_x, (y + dy * steps) % size_y
        for j, (x1, x2, y1, y2) in enumerate(quadrant_bounds):
            if x1 <= x < x2 and y1 <= y < y2:
                quadrants[j] += 1
        robots[i] = (x, y, dx, dy)
    return robots, quadrants


def puzzle1():
    return math.prod(simulate(read_input())[1].values())


def find_arrangements(robots, size_x=SIZE_X, size_y=SIZE_Y):
    all_positions = []
    t = 0
    while True:
        robots, _ = simulate(robots, steps=1)
        t += 1
        positions = get_positions(robots)
        if positions in all_positions:
            return t
        all_positions.append(positions)


def puzzle2(stdscr):
    t = 0
    robots = read_input()
    max_t = find_arrangements(robots)
    robots, _ = simulate(robots, steps=t)
    while True:
        robots, _ = simulate(robots, steps=1)
        t += 1
        positions = get_positions(robots)
        vertical_robots = sum(1 for y in range(SIZE_Y) if positions[(y, 52)] > 0)
        if vertical_robots > 30:
            display(stdscr, positions, t)
            stdscr.getkey()
        if t > max_t:
            break


if __name__ == "__main__":
    wrapper(puzzle2)
