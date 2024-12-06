def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[c for c in l.strip()] for l in f.readlines()]


def find_start(lab_matrix, start="^"):
    for i, row in enumerate(lab_matrix):
        for j, tile in enumerate(row):
            if tile == start:
                return i, j


def get_directions(start=(-1, 0)):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    start_index = directions.index(start)
    while True:
        for di, dj in directions[start_index:] + directions[:start_index]:
            yield (di, dj)


def in_bounds(i, j, m):
    return 0 <= i < len(m) and 0 <= j < len(m[0])


def patrol(lab_matrix, i, j, direction):
    visited = {}
    directions = get_directions(start=direction)
    di, dj = next(directions)
    cycle = False
    t = 0
    while True:
        if (i, j, di, dj) in visited:
            cycle = True
            break
        visited[(i, j, di, dj)] = t
        t += 1
        ii, jj = i + di, j + dj
        if not in_bounds(ii, jj, lab_matrix):
            break
        while lab_matrix[ii][jj] in "#O":
            di, dj = next(directions)
            ii, jj = i + di, j + dj
        i, j = ii, jj
    return visited, cycle


def puzzle1():
    lab_matrix = read_input()
    i, j = find_start(lab_matrix)
    visited, _ = patrol(lab_matrix, i, j, direction=(-1, 0))
    return len({(i, j) for (i, j, _, _) in visited})


def puzzle2():
    lab_matrix = read_input()
    start_i, start_j = find_start(lab_matrix)
    visited, _ = patrol(lab_matrix, start_i, start_j, direction=(-1, 0))
    obstructions = {}
    for i, j, di, dj in sorted(visited.keys(), key=lambda x: visited[x]):
        if (i, j) != (start_i, start_j) and (i, j) not in obstructions:
            lab_matrix[i][j] = "O"
            _, cycle = patrol(lab_matrix, i - di, j - dj, direction=(di, dj))
            obstructions[(i, j)] = int(cycle)
            lab_matrix[i][j] = "."
    return sum(obstructions.values())


if __name__ == "__main__":
    print(puzzle2())
