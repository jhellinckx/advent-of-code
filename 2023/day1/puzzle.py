import math


def get_lines(filename="input.txt"):
    with open(filename, "r") as f:
        return f.readlines()


def puzzle1():
    sum = 0
    for line in get_lines():
        first = None
        last = None
        for c in line:
            if c.isdigit():
                if first is None:
                    first = c
                last = c
        sum += int(f"{first}{last}")
    print(sum)


digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

digits_reversed = [d[::-1] for d in digits]


def get_first_digit_int(line):
    for i, c in enumerate(line):
        if c.isdigit():
            return i, c
    return math.inf, None


def get_first_digit_str(line, digit_strings):
    first_index = math.inf
    first_digit = None
    for digit, digit_string in enumerate(digit_strings):
        index = line.find(digit_string)
        if index >= 0 and index < first_index:
            first_index = index
            first_digit = digit
    return first_index, first_digit


def get_first_digit(line, digit_strings):
    first_int_index, first_int_digit = get_first_digit_int(line)
    first_str_index, first_str_digit = get_first_digit_str(line, digit_strings)
    return first_int_digit if first_int_index < first_str_index else first_str_digit


def puzzle2():
    sum = 0
    for line in get_lines():
        first = get_first_digit(line, digits)
        line_reversed = line[::-1]
        last = get_first_digit(line_reversed, digits_reversed)
        sum += int(f"{first}{last}")
    print(sum)


if __name__ == "__main__":
    puzzle2()
