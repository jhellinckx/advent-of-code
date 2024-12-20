def read_input(filename="input.txt"):
    with open(filename) as f:
        towels = f.readline().strip().split(", ")
        f.readline()
        designs = [l.strip() for l in f.readlines()]
        return towels, designs


def match_design(design, towels, max_len, seen={}):
    if design == "":
        return 1
    if design in seen:
        return seen[design]
    solutions = sum(
        match_design(design[i:], towels, max_len, seen)
        for i in range(max_len + 1)
        if design[:i] in towels and len(design[:i]) == i
    )
    seen[design] = solutions
    return solutions


def puzzle1():
    towels, designs = read_input()
    return sum(
        1
        for d in designs
        if match_design(d, set(towels), max(len(t) for t in towels)) > 0
    )


def puzzle2():
    towels, designs = read_input()
    return sum(
        match_design(d, set(towels), max(len(t) for t in towels)) for d in designs
    )


if __name__ == "__main__":
    print(puzzle2())
