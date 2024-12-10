import math
from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[c for c in l.strip()] for l in f.readlines()]


def to_cartesian(i, j, m):
    return j, len(m) - i - 1


def to_matrix_index(x, y, m):
    return len(m) - y - 1, x


def in_bounds(i, j, m):
    return 0 <= i < len(m) and 0 <= j < len(m[0])


def line_from_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:
        return float("inf"), x1
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def points_at_distance_on_line(p, d, m, b):
    x, y = p
    if m == 0:
        return [(x + d, y), (x - d, y)]
    if m == float("inf"):
        return [(x, y + d), (x, y - d)]
    x1 = x + d / (1 + m**2) ** 0.5
    y1 = m * x1 + b
    x2 = x - d / (1 + m**2) ** 0.5
    y2 = m * x2 + b
    return [(x1, y1), (x2, y2)]


def find_antinodes(get_candidates, validate_candidate):
    map = read_input()
    antennas = defaultdict(list)
    antinodes = set()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != ".":
                antennas[map[i][j]].append(to_cartesian(i, j, map))
    for _, points in antennas.items():
        pairs = [(p1, p2) for p1 in points for p2 in points if p1 != p2]
        for p1, p2 in pairs:
            m, b = line_from_points(p1, p2)
            d = distance(p1, p2)
            candidates = defaultdict(set)
            for p, dd in get_candidates(p1, p2, d, map):
                for (px, py) in points_at_distance_on_line(p, dd, m, b):
                    px = round(px, 2)
                    py = round(py, 2)
                    if px.is_integer() and py.is_integer():
                        px = int(px)
                        py = int(py)
                        candidates[(px, py)].add(dd)
            for (px, py), ds in candidates.items():
                if validate_candidate((px, py), ds, d):
                    antinodes.add(to_matrix_index(px, py, map))

    antinodes = [(i, j) for i, j in antinodes if in_bounds(i, j, map)]
    return len(antinodes)


def puzzle1():
    return find_antinodes(
        get_candidates=lambda p1, p2, d, m: [
            (p1, d),
            (p1, 2 * d),
            (p2, d),
            (p2, 2 * d),
        ],
        validate_candidate=lambda p, ds, d: (ds == {d, 2 * d}),
    )


def puzzle2():
    return find_antinodes(
        get_candidates=lambda p1, p2, d, m: [
            (p1, 0),
            (p2, 0),
            *[(p1, d * dd) for dd in range(len(m))],  # works since m is a square matrix
        ],
        validate_candidate=lambda p, ds, d: True,
    )


if __name__ == "__main__":
    print(puzzle2())
