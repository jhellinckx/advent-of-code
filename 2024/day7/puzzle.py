OP_SUM = int.__add__
OP_MUL = int.__mul__
OP_CONCAT = lambda a, b: int(f"{a}{b}")


def read_input(filename="input.txt"):
    equations = []
    with open(filename) as f:
        for l in f.readlines():
            target, digits = l.split(": ")
            equations.append((int(target), [int(d) for d in digits.split(" ")]))
    return equations


def solvable(target, digits, current_total, allowed_operators):
    if not digits:
        return target == current_total
    else:
        for operator in allowed_operators:
            if (new_total := operator(current_total, digits[0])) > target:
                continue
            elif solvable(target, digits[1:], new_total, allowed_operators):
                return True
        return False


def solvable_targets(allowed_operators):
    return [
        target
        for target, digits in read_input()
        if solvable(target, digits[1:], digits[0], allowed_operators)
    ]


def puzzle1():
    return sum(solvable_targets([OP_SUM, OP_MUL]))


def puzzle2():
    return sum(solvable_targets([OP_SUM, OP_MUL, OP_CONCAT]))


if __name__ == "__main__":
    print(puzzle2())
