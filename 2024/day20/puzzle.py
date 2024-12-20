def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[c for c in l.strip()] for l in f.readlines()]


def find_tile(m, tile):
    for i, row in enumerate(m):
        for j, c in enumerate(row):
            if c == tile:
                return i, j


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_track_distances(m, end):
    distances = {}
    visited = set()
    queue = [(end, 0)]
    while queue:
        (i, j), d = queue.pop(0)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        distances[i, j] = d
        for di, dj in DIRECTIONS:
            if (
                0 <= i + di < len(m)
                and 0 <= j + dj < len(m[0])
                and m[i + di][j + dj] != "#"
            ):
                queue.append(((i + di, j + dj), d + 1))
    return distances


def add_cheats(
    m, start, cheats, start_d, end_d, max_cheat_len, max_distance, real_distance
):
    if start not in start_d:
        return
    start_distance = start_d[start]
    queue = [(*start, 0)]
    visited = set()
    while queue:
        i, j, d = queue.pop(0)
        if d > max_cheat_len:
            continue
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if (
            m[i][j] != "#"
            and (i, j) in end_d
            and (cheat_distance := start_distance + d + end_d[i, j]) <= max_distance
        ):
            cheats[(start, (i, j))] = real_distance - cheat_distance
        for di, dj in DIRECTIONS:
            if (
                0 <= i + di < len(m)
                and 0 <= j + dj < len(m[0])
                and (i + di, j + dj) not in visited
            ):
                queue.append((i + di, j + dj, d + 1))


def find_cheats(m, start, end, min_gain, max_cheat_len):
    start_distances = get_track_distances(m, start)
    end_distances = get_track_distances(m, end)
    real_distance = end_distances[start]
    max_distance = real_distance - min_gain
    cheats = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != "#":
                add_cheats(
                    m,
                    (i, j),
                    cheats,
                    start_distances,
                    end_distances,
                    max_cheat_len,
                    max_distance,
                    real_distance,
                )
    return cheats


def puzzle1():
    m = read_input()
    start = find_tile(m, "S")
    end = find_tile(m, "E")
    cheats = find_cheats(m, start, end, 100, 2)
    return len(cheats)


def puzzle2():
    m = read_input()
    start = find_tile(m, "S")
    end = find_tile(m, "E")
    cheats = find_cheats(m, start, end, 100, 20)
    return len(cheats)


if __name__ == "__main__":
    print(puzzle2())
