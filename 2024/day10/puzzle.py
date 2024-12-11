from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[int(d) for d in l.strip()] for l in f.readlines()]


def find_trailheads(map):
    return [
        (i, j) for i in range(len(map)) for j in range(len(map[0])) if map[i][j] == 0
    ]


def in_bounds(i, j, map):
    return 0 <= i < len(map) and 0 <= j < len(map[0])


def get_children(i, j, map):
    return [
        (ii, jj)
        for ii, jj in [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1),
        ]
        if in_bounds(ii, jj, map) and map[ii][jj] == map[i][j] + 1
    ]


def tree_search(map, start, target):
    start_i, start_j = start
    targets = defaultdict(int)
    queue = [(start_i, start_j)]
    while queue:
        i, j = queue.pop(0)
        if map[i][j] == target:
            targets[(i, j)] += 1
        queue.extend([(ii, jj) for ii, jj in get_children(i, j, map)])
    return targets


def puzzle1():
    topographic_map = read_input()
    return sum(
        len(tree_search(topographic_map, head, 9))
        for head in find_trailheads(topographic_map)
    )


def puzzle2():
    topographic_map = read_input()
    return sum(
        sum(tree_search(topographic_map, head, 9).values())
        for head in find_trailheads(topographic_map)
    )


if __name__ == "__main__":
    print(puzzle2())
