import re
import numpy as np


def read_input(filename="input.txt"):
    systems = []
    with open(filename) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            eq_str = lines[i]
            i += 1
            if eq_str.startswith("Button A"):
                eq_str += lines[i] + lines[i + 1]
                i += 2
                ax1, ax2, ay1, ay2, b1, b2 = [
                    int(n)
                    for n in re.search(
                        r"A: X\+(\d+), Y\+(\d+)[\s\S]*B: X\+(\d+), Y\+(\d+)[\s\S]*X=(\d+), Y=(\d+)",
                        eq_str,
                    ).groups()
                ]
                systems.append((np.array([[ax1, ay1], [ax2, ay2]]), np.array([b1, b2])))
    return systems


def solve(max, add_b=0):
    systems = read_input()
    s = 0
    for a, b in systems:
        x, y = np.linalg.solve(a, b + add_b)
        x, y = round(x, 2), round(y, 2)
        if x.is_integer() and y.is_integer() and 0 <= x <= max and 0 <= y <= max:
            s += int(x) * 3 + int(y) * 1
    return s


def puzzle1():
    return solve(max=100)


def puzzle2():
    return solve(max=float("inf"), add_b=10000000000000)


if __name__ == "__main__":
    print(puzzle2())
