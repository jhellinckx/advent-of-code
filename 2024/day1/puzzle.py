from collections import Counter


def puzzle1():
    with open("input.txt") as f:
        return sum(
            abs(a - b)
            for a, b in zip(
                *[
                    sorted(l)
                    for l in zip(
                        *[(int(d) for d in l.split("   ")) for l in f.readlines()]
                    )
                ]
            )
        )


def puzzle2():
    with open("input.txt") as f:
        l1, l2 = zip(*[(int(d) for d in l.split("   ")) for l in f.readlines()])
        l2 = Counter(l2)
        return sum(a * l2[a] for a in l1)


if __name__ == "__main__":
    print(puzzle2())
