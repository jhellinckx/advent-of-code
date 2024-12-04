from functools import reduce


def get_races(filename="input.txt"):
    parse = lambda line: list(
        map(
            int,
            filter(str.isdigit, map(str.strip, line.split(":")[1].split(" "))),
        )
    )
    with open(filename, "r") as f:
        times = parse(f.readline())
        distances = parse(f.readline())
    return times, distances


def race_wins(time, record_distance):
    wins = 0
    for press_time in range(1, time):
        move_time = time - press_time
        boat_speed = press_time
        boat_distance = boat_speed * move_time
        if boat_distance > record_distance:
            wins += 1
    return wins


def puzzle1():
    races = zip(*get_races())
    all_wins = []
    for time, record_distance in races:
        all_wins.append(race_wins(time, record_distance))
    print(reduce(lambda x, y: x * y, all_wins))


def puzzle2():
    times, distances = get_races()
    time = int("".join(map(str, times)))
    record_distance = int("".join(map(str, distances)))
    print(race_wins(time, record_distance))


if __name__ == "__main__":
    puzzle2()
