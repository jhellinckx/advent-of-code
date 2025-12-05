def read_input(filename="input.txt"):
    ranges = []
    ids = []
    with open(filename) as f:
        while (l := f.readline().strip()) != "":
            ranges.append(tuple(int(d) for d in l.split("-")))
        ids = [int(d.strip()) for d in f.readlines()]
    return list(set(ranges)), ids


def puzzle1():
    ranges, ids = read_input()
    return len({i for i in ids for l, u in ranges if l <= i <= u})


def remove_overlaps(ranges):
    for i, (l1, u1) in enumerate(ranges):
        for j, (l2, u2) in enumerate(ranges):
            if i != j:
                if l1 >= l2 and u1 <= u2:
                    return remove_overlaps(ranges[:i] + ranges[i + 1 :])
                if l2 <= l1 <= u2:
                    ranges[i] = (u2 + 1, u1)
                    return remove_overlaps(ranges)
                if l2 <= u1 <= u2:
                    ranges[i] = (l1, l2 - 1)
                    return remove_overlaps(ranges)
    return ranges


def puzzle2():
    ranges, _ = read_input()
    return sum(u - l + 1 for l, u in remove_overlaps(ranges))


if __name__ == "__main__":
    print(puzzle2())
