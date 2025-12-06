import re
from functools import reduce
from operator import mul, add


def read_input(filename="input.txt", dtype=int):
    with open("input.txt") as f:
        lines = list(f.readlines())
        ops = [(m.group(), m.start()) for m in re.finditer(r"[*+]", lines[-1])]
        ops, pos = zip(*ops)
        ranges = list(zip(pos, pos[1:] + (len(lines[-1]) + 1,)))
        digits = [[dtype(line[s : e - 1]) for s, e in ranges] for line in lines[:-1]]
        ops = [(add, 0) if op == "+" else (mul, 1) for op in ops]
        return zip(*digits), ops


def solve(all_digits, ops):
    return sum(reduce(f, digits, init) for digits, (f, init) in zip(all_digits, ops))


def puzzle1():
    all_digits, ops = read_input(dtype=int)
    return solve(all_digits, ops)


def puzzle2():
    all_digits, ops = read_input(dtype=str)
    all_digits = [[int("".join(col)) for col in zip(*digits)] for digits in all_digits]
    return solve(all_digits, ops)


if __name__ == "__main__":
    print(puzzle2())
