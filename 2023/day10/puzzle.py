from shapely import Point, Polygon


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[c for c in l] for l in f.readlines()]


def in_bounds(i, j, tiles):
    return 0 <= i < len(tiles) and 0 <= j < len(tiles[0])


def get_adjacents(i, j, tiles):
    return [
        (ii, jj)
        for ii, jj in {
            ".": [],
            "|": [(i + 1, j), (i - 1, j)],
            "-": [(i, j + 1), (i, j - 1)],
            "L": [(i - 1, j), (i, j + 1)],
            "J": [(i - 1, j), (i, j - 1)],
            "7": [(i + 1, j), (i, j - 1)],
            "F": [(i + 1, j), (i, j + 1)],
            "S": get_start_adjacents(i, j, tiles),
        }[tiles[i][j]]
        if in_bounds(ii, jj, tiles)
    ]


def get_start_adjacents(i, j, tiles):
    start = (i, j)
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ii, jj = i + di, j + dj
        if in_bounds(ii, jj, tiles):
            if start in get_adjacents(ii, jj, tiles):
                yield (ii, jj)


def find_start(tiles, start="S"):
    for i, row in enumerate(tiles):
        for j, tile in enumerate(row):
            if tile == start:
                return i, j


def bfs(tiles):
    start_i, start_j = find_start(tiles)
    visited = {}
    queue = [(start_i, start_j, 0)]
    while queue:
        i, j, d = queue.pop(0)
        if (i, j) in visited:
            continue
        visited[(i, j)] = d
        queue.extend(
            [
                (ii, jj, d + 1)
                for ii, jj in get_adjacents(i, j, tiles)
                if (ii, jj) not in visited
            ]
        )
    return visited


def dfs(tiles):
    start_i, start_j = find_start(tiles)
    visited = {}
    stack = [(start_i, start_j, 0)]
    while stack:
        i, j, d = stack.pop()
        if (i, j) in visited:
            continue
        visited[(i, j)] = d
        stack.extend(
            [
                (ii, jj, d + 1)
                for ii, jj in get_adjacents(i, j, tiles)
                if (ii, jj) not in visited
            ]
        )
    return visited


def to_cartesian(i, j, tiles):
    return j, len(tiles) - i - 1


def puzzle1(filename="input.txt"):
    tiles = read_input(filename)
    visited = bfs(tiles)
    return max(visited.values())


def puzzle2(filename="input.txt"):
    tiles = read_input(filename)
    visited = dfs(tiles)
    loop_points = visited.keys()
    candidate_points = [
        Point(*to_cartesian(i, j, tiles))
        for i in range(len(tiles))
        for j in range(len(tiles[0]))
        if (i, j) not in loop_points
    ]
    loop_polygon = Polygon([to_cartesian(i, j, tiles) for i, j in loop_points])
    return sum(1 for p in candidate_points if loop_polygon.contains(p))


if __name__ == "__main__":
    print(puzzle2("input.txt"))
