import re

from functools import reduce


def puzzle1():
    with open("input.txt") as f:
        return sum(
            int(a) * int(b)
            for a, b in re.findall(r"mul\((\d+),(\d+)\)", "".join(f.readlines()))
        )


def puzzle2():
    do = True
    s = 0
    with open("input.txt") as f:
        for a, b, op_do, op_dont in re.findall(
            r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", "".join(f.readlines())
        ):
            if not a:
                do = op_do or not op_dont
            elif do:
                s += int(a) * int(b)
    return s


if __name__ == "__main__":
    print(puzzle2())
