def read_input(filename="input.txt"):
    with open(filename) as f:
        return [r.split("-") for r in f.readline().split(",")]


def puzzle1():
    return sum(
        [
            i
            for start, end in read_input()
            for i in range(int(start), int(end) + 1)
            if (s := str(i))[: len(s) // 2] == s[len(s) // 2 :]
        ]
    )


def puzzle2():
    ranges = read_input()
    ids = []
    for start, end in ranges:
        for i in range(int(start), int(end) + 1):
            s = str(i)
            for j in range(1, len(s) // 2 + 1):
                if len(s) % j == 0:
                    ss = [s[max(0, k - j) : k] for k in range(j, len(s) + j, j)]
                    if len(set(ss)) == 1 and len(ss) >= 2:
                        ids.append(i)
                        break
    return sum(ids)


if __name__ == "__main__":
    print(puzzle2())
