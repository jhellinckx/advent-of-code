def read_input(filename="input.txt"):
    with open(filename) as f:
        return [[c for c in l.strip()] for l in f.readlines()]


DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
MAX_ROLLS = 3
PAPER_ROLL = "@"


def get_rolls(m):
    return {
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


def puzzle1():
    return sum(1 for c in get_rolls(read_input()).values() if c <= MAX_ROLLS)


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
    rolls = get_rolls(read_input())
    lifted = set()
    for r in [r for r, c in rolls.items() if c <= MAX_ROLLS]:
        lift_roll(r, rolls, lifted)
    return len(lifted)


if __name__ == "__main__":
    print(puzzle1())
