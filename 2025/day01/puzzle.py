import operator


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def puzzle1():
    rotations = read_input()
    dial_digits = [None] * len(rotations)
    prev_digit = 50
    for i, rotation in enumerate(rotations):
        op = operator.sub if rotation.startswith("L") else operator.add
        dial_digits[i] = op(prev_digit, int(rotation[1:])) % 100
        prev_digit = dial_digits[i]
    return len([i for i in dial_digits if i == 0])


def puzzle2():
    rotations = read_input()
    prev_digit = 50
    zeros = 0
    for rotation in rotations:
        left = rotation.startswith("L")
        op = operator.sub if left else operator.add
        num_rotations = int(rotation[1:])
        d = prev_digit
        if left and d != 0:
            d = 100 - d
        zeros += (d + num_rotations) // 100
        prev_digit = op(prev_digit, num_rotations) % 100
    return zeros


if __name__ == "__main__":
    print(puzzle2())
