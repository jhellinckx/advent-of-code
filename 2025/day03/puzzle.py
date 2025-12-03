def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[int(c) for c in l.strip()] for l in f.readlines()]


def puzzle1():
    banks = read_input()
    joltages = []
    for bank in banks:
        battery_left = max(bank)
        i = bank.index(battery_left)
        if i == (len(bank) - 1):
            battery_right = battery_left
            battery_left = max(bank[: len(bank) - 1])
        else:
            battery_right = max(bank[i + 1 :])
        joltage = int(f"{battery_left}{battery_right}")
        joltages.append(joltage)
    return sum(joltages)


def puzzle2():
    banks = read_input()
    bank_joltages = []
    num_batteries = 12
    for bank in banks:
        joltages = []
        curr_bank = bank
        for i in range(1, num_batteries + 1):
            joltage = max(curr_bank[: len(curr_bank) - (num_batteries - i)])
            joltages.append(str(joltage))
            j = curr_bank.index(joltage)
            curr_bank = curr_bank[j + 1 :]
        bank_joltages.append(int("".join(joltages)))
    return sum(bank_joltages)


if __name__ == "__main__":
    print(puzzle2())
