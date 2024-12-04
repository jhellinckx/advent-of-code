def get_engine_schematic(filename="input.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()
        lines = map(str.strip, lines)
        return list(map(list, lines))


def is_symbol(val):
    return val != "." and not val.isdigit()


def in_bounds(matrix, i, j):
    if i < 0 or j < 0:
        return False
    try:
        matrix[i][j]
        return True
    except IndexError:
        return False


def get_adjacents(engine, i, j):
    adjacents = []
    moves = [-1, 0, 1]
    for dx in moves:
        for dy in moves:
            if dx == dy == 0:
                continue
            new_i, new_j = i + dx, j + dy
            if in_bounds(engine, new_i, new_j):
                adjacents.append((new_i, new_j))
    return adjacents


def expand_part(engine, i, j, delta):
    while in_bounds(engine, i, j + delta) and engine[i][j + delta].isdigit():
        j = j + delta
    return j


def extract_part(engine, i, j):
    start = expand_part(engine, i, j, delta=-1)
    end = expand_part(engine, i, j, delta=1)
    part = int("".join(engine[i][start : end + 1]))
    for j in range(start, end + 1):
        engine[i][j] = "."
    return part


def find_parts(engine, i, j):
    adjacents = get_adjacents(engine, i, j)
    parts = []
    for adj_i, adj_j in adjacents:
        if engine[adj_i][adj_j].isdigit():
            part = extract_part(engine, adj_i, adj_j)
            parts.append(part)
    return parts


def puzzle1():
    engine = get_engine_schematic()
    all_parts = []
    for i in range(len(engine)):
        for j in range(len(engine[i])):
            if is_symbol(engine[i][j]):
                all_parts += find_parts(engine, i, j)
    print(sum(all_parts))


def is_gear(val):
    return val == "*"


def puzzle2():
    engine = get_engine_schematic()
    gear_ratios = []
    for i in range(len(engine)):
        for j in range(len(engine[i])):
            if is_gear(engine[i][j]):
                parts = find_parts(engine, i, j)
                if len(parts) == 2:
                    gear_ratios.append(parts[0] * parts[1])
    print(sum(gear_ratios))


if __name__ == "__main__":
    puzzle2()
