import re
import numpy as np
from functools import partial
from itertools import batched


def solve(max, add_b=0):
    return int(
        sum(
            sum(
                np.array([3, 1]) * x
                if all(xi.is_integer() for xi in x) and all(0 <= xi <= max for xi in x)
                else np.array([0, 0])
            )
            for x in [
                np.array(
                    list(map(partial(round, ndigits=2), np.linalg.solve(a, b + add_b)))
                )
                for a, b in [
                    (np.array([[ax1, ay1], [ax2, ay2]]), np.array([b1, b2]))
                    for ax1, ax2, ay1, ay2, b1, b2 in batched(
                        [int(s) for s in re.findall(r"\d+", open("input.txt").read())],
                        6,
                    )
                ]
            ]
        )
    )


def puzzle1():
    return solve(max=100)


def puzzle2():
    return solve(max=float("inf"), add_b=10000000000000)


if __name__ == "__main__":
    print(puzzle2())
