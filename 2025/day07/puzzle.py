from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename) as f:
        m = [[c for c in l.strip()] for l in f.readlines()]
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == START:
                    return m, (i, j)


SPLITTER = "^"
START = "S"
LEFT = "L"
RIGHT = "R"
TOTAL = "T"


def is_splitter(m, i, j):
    return i < len(m) and m[i][j] == SPLITTER


def get_moves(m, i, j, path):
    if is_splitter(m, i + 1, j):
        moves = [
            (i + 1, j - 1, path + [(i + 1, j, LEFT)]),
            (i + 1, j + 1, path + [(i + 1, j, RIGHT)]),
        ]
    else:
        moves = [(i + 1, j, path)]
    return [(i, j, p) for (i, j, p) in moves if 0 <= i < len(m) and 0 <= j < len(m[i])]


def puzzle1():
    m, (i, j) = read_input()
    splits = 0
    queue = [(i, j, [])]
    seen = set()
    while queue:
        i, j, p = queue.pop(0)
        if (i, j) in seen:
            continue
        seen.add((i, j))
        moves = get_moves(m, i, j, p)
        if len(moves) >= 2:
            splits += 1
        queue += moves
    return splits


def update_timelines(timelines, path, t):
    (si, sj, sd) = path[-1]  # Last splitter pos + direction
    timelines[(si, sj)][sd] = t  # Update last splitter timelines count
    left_timelines = timelines[(si, sj)].get(LEFT, None)
    right_timelines = timelines[(si, sj)].get(RIGHT, None)
    if left_timelines is not None and right_timelines is not None:
        total = left_timelines + right_timelines
        timelines[(si, sj)][TOTAL] = total
        if path[:-1]:
            update_timelines(timelines, path[:-1], total)


def puzzle2():
    m, (i, j) = read_input()
    queue = [(i, j, [])]
    all_timelines = defaultdict(dict)
    while queue:
        i, j, path = queue.pop()
        if i == len(m) - 1:
            update_timelines(all_timelines, path, 1)
        elif (
            is_splitter(m, i + 1, j)
            and (t := all_timelines[(i + 1, j)].get(TOTAL, None)) is not None
        ):
            update_timelines(all_timelines, path, t)
        else:
            queue += get_moves(m, i, j, path)
    return max(t[TOTAL] for t in all_timelines.values())


if __name__ == "__main__":
    print(puzzle2())
