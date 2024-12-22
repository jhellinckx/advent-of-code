import re
import heapq


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [list(l.strip()) for l in f.readlines()]


def as_map(matrix):
    return {
        (i, j): c
        for i, row in enumerate(matrix)
        for j, c in enumerate(row)
        if c is not None
    }


def inv_map(map):
    return {v: k for k, v in map.items()}


numeric_keypad = as_map(
    [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"],
    ]
)
numeric_keypad_inv = inv_map(numeric_keypad)

directional_keypad = as_map(
    [
        [None, "^", "A"],
        ["<", "v", ">"],
    ]
)
directional_keypad_inv = inv_map(directional_keypad)


min_cost_cache = {}


def min_cost(map, start, end, max_robots, robot=None):
    if robot is None:
        robot = max_robots
    if robot != max_robots and (start, end, robot) in min_cost_cache:
        return min_cost_cache[(start, end, robot)]
    queue = []
    heapq.heappush(queue, (0, (start, [])))
    visited = set()
    while queue:
        c, ((i, j), dirs) = heapq.heappop(queue)
        current_dir = dirs[-1] if dirs else None
        if (i, j, current_dir) in visited:
            continue
        visited.add((i, j, current_dir))
        if (i, j) == end:
            if current_dir != "A":
                end_cost = (
                    1
                    if robot == 0
                    else min_cost(
                        directional_keypad,
                        directional_keypad_inv[current_dir or "A"],
                        directional_keypad_inv["A"],
                        max_robots,
                        robot - 1,
                    )
                )
                heapq.heappush(queue, (c + end_cost, ((i, j), dirs + ["A"])))
            else:
                if robot != max_robots:
                    min_cost_cache[(start, end, robot)] = c
                return c
        for di, dj, new_dir in [(0, 1, ">"), (0, -1, "<"), (1, 0, "v"), (-1, 0, "^")]:
            if (i + di, j + dj) in map:
                dir_cost = (
                    1
                    if robot == 0
                    else min_cost(
                        directional_keypad,
                        directional_keypad_inv[current_dir or "A"],
                        directional_keypad_inv[new_dir],
                        max_robots,
                        robot - 1,
                    )
                )
                heapq.heappush(
                    queue, (c + dir_cost, ((i + di, j + dj), dirs + [new_dir]))
                )


def find_code_cost(code, robots):
    return sum(
        min_cost(
            numeric_keypad, numeric_keypad_inv[start], numeric_keypad_inv[end], robots
        )
        for start, end in zip(["A"] + code, code)
    )


def numeric_part(s):
    return int("".join(re.findall(r"\d+", s)))


def puzzle1():
    return sum(
        numeric_part("".join(code)) * find_code_cost(code, 2) for code in read_input()
    )


def puzzle2():
    return sum(
        numeric_part("".join(code)) * find_code_cost(code, 25) for code in read_input()
    )


if __name__ == "__main__":
    print(puzzle2())
