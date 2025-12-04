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
    return sum(1 for count in get_rolls(read_input()).values() if count <= MAX_ROLLS)


def lift_roll(roll, rolls, lifted=set()):
    if roll not in lifted:
        lifted.add(roll)
        i, j = roll
        for di, dj in DELTAS:
            adj = i + di, j + dj
            if adj in rolls and adj not in lifted:
                rolls[adj] -= 1
                if rolls[adj] <= MAX_ROLLS:
                    lift_roll(adj, rolls, lifted)


def puzzle2():
    rolls = get_rolls(read_input())
    lifted = set()
    for roll in [roll for roll, count in rolls.items() if count <= MAX_ROLLS]:
        lift_roll(roll, rolls, lifted)
    return len(lifted)


if __name__ == "__main__":
    print(puzzle2())
