import math
from functools import partial

sign = partial(math.copysign, 1)


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[int(d) for d in l.strip().split(" ")] for l in f.readlines()]


def is_safe(report, tolerate=False):
    s = sign(report[1] - report[0])
    for i, (a, b) in enumerate(zip(report, report[1:])):
        diff = b - a
        if sign(diff) != s or not 1 <= abs(diff) <= 3:
            if tolerate:
                return int(
                    any(
                        [
                            is_safe(report[: i - 1] + report[i:], tolerate=False),
                            is_safe(report[:i] + report[i + 1 :], tolerate=False),
                            is_safe(report[: i + 1] + report[i + 2 :], tolerate=False),
                        ]
                    )
                )
            else:
                return 0
    return 1


def puzzle1():
    reports = read_input()
    return sum(is_safe(report, tolerate=False) for report in reports)


def puzzle2():
    reports = read_input()
    return sum(is_safe(report, tolerate=True) for report in reports)


if __name__ == "__main__":
    print(puzzle2())
