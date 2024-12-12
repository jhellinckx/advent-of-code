from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[c for c in l.strip()] for l in f.readlines()]


NO_COLOR = 0


def print_fences(regions, m):
    from termcolor import cprint, COLORS, HIGHLIGHTS
    import random

    colors = {i: random.choice(list(COLORS.keys())) for i in range(1, 1000)}
    highlights = {i: random.choice(list(HIGHLIGHTS.keys())) for i in range(1, 1000)}
    size_i = max(i for region in regions.values() for i, _, _ in region) + 1
    size_j = max(j for region in regions.values() for _, j, _ in region) + 1
    fences = [[0 for _ in range(size_j)] for _ in range(size_i)]
    for color, region in regions.items():
        for i, j, n in region:
            fences[i][j] = (color, n)
    for i in range(size_i):
        for j in range(size_j):
            color, n = fences[i][j]
            s = f"{m[i, j][0]}{n}"
            cprint(f"{s:>4}", colors[color], highlights[color], end="")
        print()


def color_regions(m, i=0, j=0, regions=defaultdict(list), region_color=1):
    queue = [(i, j)]
    region_val = m[i, j][0]
    new_regions = []
    while queue:
        i, j = queue.pop(0)
        val, color = m[i, j]
        if color != NO_COLOR:
            continue
        if val != region_val:
            new_regions.append((i, j))
            continue
        m[i, j][1] = region_color
        adjacents = [
            (ii, jj)
            for ii, jj in [
                (i + di, j + dj) for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            ]
            if (ii, jj) in m
        ]
        queue.extend([(ii, jj) for ii, jj in adjacents if m[ii, jj][1] == NO_COLOR])
        regions[region_color].append(
            (i, j, 4 - sum([1 for ii, jj in adjacents if m[ii, jj][0] == region_val]))
        )
    for (i, j) in new_regions:
        if m[i, j][1] == NO_COLOR:
            region_color += 1
            _, region_color = color_regions(m, i, j, regions, region_color)
    return regions, region_color


def get_fences(i, j, m):
    return [
        f
        for ii, jj, f in [
            (i + di, j + dj, f)
            for di, dj, f in [(1, 0, "S"), (-1, 0, "N"), (0, 1, "E"), (0, -1, "W")]
        ]
        if (ii, jj) not in m or m[ii, jj][0] != m[i, j][0]
    ]


def get_sides(region, m):
    region = {(i, j): get_fences(i, j, m) for i, j, _ in region}
    visited = set()
    sides = 0
    queue = [(i, j, f) for (i, j), fences in region.items() for f in fences]
    while queue:
        i, j, f = queue.pop(0)
        if (i, j, f) in visited:
            continue
        visited.add((i, j, f))

        def get_adj_walls(i, j, f):
            return [
                (i + di, j + dj)
                for di, dj in {
                    "N": [(0, 1), (0, -1)],
                    "S": [(0, 1), (0, -1)],
                    "E": [(1, 0), (-1, 0)],
                    "W": [(1, 0), (-1, 0)],
                }[f]
                if (i + di, j + dj) in region
                and f in region[i + di, j + dj]
                and (i + di, j + dj, f) not in visited
            ]

        sides += 1
        adj_walls = get_adj_walls(i, j, f)
        while adj_walls:
            ii, jj = adj_walls.pop(0)
            visited.add((ii, jj, f))
            adj_walls.extend(get_adj_walls(ii, jj, f))
    return sides


def puzzle1():
    plots = read_input()
    m = {
        (i, j): [plots[i][j], NO_COLOR]
        for i in range(len(plots))
        for j in range(len(plots[0]))
    }
    regions, _ = color_regions(m)
    return sum(
        (len(region) * sum(n for _, _, n in region)) for region in regions.values()
    )


def puzzle2():
    plots = read_input()
    m = {
        (i, j): [plots[i][j], NO_COLOR]
        for i in range(len(plots))
        for j in range(len(plots[0]))
    }
    regions, _ = color_regions(m)
    return sum(get_sides(region, m) * len(region) for region in regions.values())


if __name__ == "__main__":
    print(puzzle2())
