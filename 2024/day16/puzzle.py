import heapq
from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[c for c in l.strip()] for l in f.readlines()]


def find_tile(m, tile):
    for i, row in enumerate(m):
        for j, c in enumerate(row):
            if c == tile:
                return i, j


def cost(c, r):
    return c + abs(r) * 1000 + 1


def in_bounds(i, j, m):
    return 0 <= i < len(m) and 0 <= j < len(m[0])


def shortest_paths(m, start, end):
    i, j = start
    queue = []
    heapq.heappush(queue, (0, (i, j, 1, [(i, j)])))
    visited = defaultdict(lambda: float("inf"))
    min_cost = float("inf")
    paths = []
    while queue:
        c, (i, j, o, p) = heapq.heappop(queue)
        if c > min_cost:
            break
        if (i, j) == end:
            min_cost = c
            paths.append(p)
            continue
        if visited[i, j, o] < c:
            continue
        visited[i, j, o] = c
        for adjacent in [
            (cc, (ii, jj, oo, p + [(ii, jj)]))
            for (ii, jj, oo, cc) in [
                {
                    0: (i - 1, j, 0, cost(c, r)),
                    1: (i, j + 1, 1, cost(c, r)),
                    2: (i + 1, j, 2, cost(c, r)),
                    3: (i, j - 1, 3, cost(c, r)),
                }[(o + r) % 4]
                for r in range(-1, 3)
            ]
            if in_bounds(ii, jj, m) and m[ii][jj] != "#" and cc < visited[ii, jj, oo]
        ]:
            heapq.heappush(queue, adjacent)
    return min_cost, paths


def puzzle1():
    m = read_input()
    c, _ = shortest_paths(m, find_tile(m, "S"), find_tile(m, "E"))
    return c


def puzzle2():
    m = read_input()
    _, paths = shortest_paths(m, find_tile(m, "S"), find_tile(m, "E"))
    best_tiles = set()
    for p in paths:
        best_tiles.update(p)
    return len(best_tiles)


if __name__ == "__main__":
    print(puzzle2())
