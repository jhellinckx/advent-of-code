import re
from math import log, floor


def read_input(filename="input.txt"):
    with open(filename) as f:
        digits = [int(d) for d in re.findall(r"\d+", f.read())]
        return digits[:3], digits[3:]


def combo(operand, a, b, c):
    return (list(range(4)) + [a, b, c])[operand]


def adv(operand, a, b, c, i):
    return int(a >> combo(operand, a, b, c)), b, c, i + 2, ""


def bxl(operand, a, b, c, i):
    return a, b ^ operand, c, i + 2, ""


def bst(operand, a, b, c, i):
    return a, combo(operand, a, b, c) & 0b111, c, i + 2, ""


def jnz(operand, a, b, c, i):
    return a, b, c, operand if a else i + 2, ""


def bxc(operand, a, b, c, i):
    return a, b ^ c, c, i + 2, ""


def out(operand, a, b, c, i):
    return a, b, c, i + 2, str(combo(operand, a, b, c) & 0b111)


def bdv(operand, a, b, c, i):
    return a, int(a >> combo(operand, a, b, c)), c, i + 2, ""


def cdv(operand, a, b, c, i):
    return a, b, int(a >> combo(operand, a, b, c)), i + 2, ""


def exec_program(program, a=0, b=0, c=0, max_iter=float("inf")):
    i = 0
    output = []
    while i < len(program) - 1:
        opcode, operand = program[i], program[i + 1]
        instruction = [adv, bxl, bst, jnz, bxc, out, bdv, cdv][opcode]
        a, b, c, i, o = instruction(operand, a, b, c, i)
        if o:
            output.append(o)
        if len(output) >= max_iter:
            break
    return output, (a, b, c), a == 0


def reverse_ouput_search(program, target_output, current_output=[], a=0):
    if current_output == target_output:
        return True, a
    if len(current_output) >= len(target_output):
        return False, None
    for i in range(8):
        next_a = (a << 3) ^ i
        o, _, end = exec_program(program, a=next_a, max_iter=1)
        if not (end ^ bool(current_output)):
            return False, None
        if o[0] == target_output[len(current_output)]:
            found, next_a = reverse_ouput_search(
                program, target_output, current_output + o, next_a
            )
            if found:
                return True, next_a
    return False, None


def puzzle1():
    (a, b, c), program = read_input()
    output, _, _ = exec_program(program, a, b, c)
    return ",".join(output)


def puzzle2():
    _, program = read_input()
    target_output = [str(d) for d in program]
    return reverse_ouput_search(program, target_output[::-1])[1]


if __name__ == "__main__":
    print(puzzle2())
