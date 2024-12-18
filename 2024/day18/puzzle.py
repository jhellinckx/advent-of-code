import re
from itertools import batched


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [(int(x), int(y)) for x, y in batched(re.findall(r"\d+", f.read()), 2)]


def bfs(size_x, size_y, start, end, walls):
    queue = [(*start, 0)]
    visited = set()
    while queue:
        x, y, d = queue.pop(0)
        if (x, y) == end:
            return d
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (
                0 <= x + dx < size_x
                and 0 <= y + dy < size_y
                and (x + dx, y + dy) not in walls
            ):
                queue.append((x + dx, y + dy, d + 1))
    return None


def bs(l, greater_than):
    low, high = 0, len(l) - 1
    while low < high:
        mid = (low + high) // 2
        if greater_than(mid):
            low = mid + 1
        else:
            high = mid
    return low


def puzzle1():
    size_x, size_y = 71, 71
    start = (0, 0)
    end = (size_x - 1, size_y - 1)
    num_walls = 1024
    walls = set(read_input()[:num_walls])
    return bfs(size_x, size_y, start, end, walls)


def puzzle2():
    size_x, size_y = 71, 71
    start = (0, 0)
    end = (size_x - 1, size_y - 1)
    walls = read_input()

    def greater_than(i):
        return bfs(size_x, size_y, start, end, set(walls[: (i + 1)])) is not None

    return ",".join([str(i) for i in walls[bs(walls, greater_than)]])


if __name__ == "__main__":
    print(puzzle2())
