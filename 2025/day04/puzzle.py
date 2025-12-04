def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[c for c in l.strip()] for l in f.readlines()]


DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
MAX_ROLLS = 3
PAPER_ROLL = "@"


def print_m(m):
    for line in m:
        print("".join(line))


def puzzle1():
    m = read_input()
    return sum(
        1
        for i in range(len(m))
        for j in range(len(m[i]))
        if m[i][j] == PAPER_ROLL
        and sum(
            1
            for (di, dj) in DELTAS
            if (
                0 <= (k := i + di) < len(m)
                and 0 <= (l := j + dj) < len(m[i])
                and m[k][l] == PAPER_ROLL
            )
        )
        <= MAX_ROLLS
    )


def lift_roll(r, rolls, lifted=set()):
    if r not in lifted:
        lifted.add(r)
        i, j = r
        for di, dj in DELTAS:
            a = i + di, j + dj
            if a in rolls and a not in lifted:
                rolls[a] -= 1
                if rolls[a] <= MAX_ROLLS:
                    lift_roll(a, rolls, lifted)


def puzzle2():
    m = read_input()
    rolls = {
        (i, j): sum(
            1
            for (di, dj) in DELTAS
            if (
                0 <= (k := i + di) < len(m)
                and 0 <= (l := j + dj) < len(m[i])
                and m[k][l] == PAPER_ROLL
            )
        )
        for i in range(len(m))
        for j in range(len(m[i]))
        if m[i][j] == PAPER_ROLL
    }
    lifted = set()
    for r in [r for r, c in rolls.items() if c <= MAX_ROLLS]:
        lift_roll(r, rolls, lifted)
    return len(lifted)


if __name__ == "__main__":
    print(puzzle2())
