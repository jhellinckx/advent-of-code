from collections import defaultdict
from functools import reduce


def get_games(filename="input.txt"):
    with open(filename, "r") as f:
        return f.readlines()


def get_game_index(game):
    return int(game.split(":")[0].split(" ")[1])


def get_game_draws(game):
    sets = game.split(":")[1].split(";")
    all_draws = []
    for s in sets:
        draws = s.split(",")
        draws = list(map(str.strip, draws))
        set_draws = []
        for draw in draws:
            count, color = draw.split(" ")
            count = int(count)
            set_draws.append((count, color))
        all_draws.append(set_draws)
    return all_draws


DEFAULT_BAG_CONTENT = {"red": 12, "green": 13, "blue": 14}


def puzzle1(bag_content=DEFAULT_BAG_CONTENT):
    games = get_games()
    total = 0
    for game in games:
        all_draws = get_game_draws(game)
        possible = True
        for draws in all_draws:
            for count, color in draws:
                if count > bag_content[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            total += get_game_index(game)
    print(total)


def puzzle2():
    games = get_games()
    total = 0
    for game in games:
        all_draws = get_game_draws(game)
        mins = defaultdict(int)
        for draws in all_draws:
            for count, color in draws:
                if count > mins[color]:
                    mins[color] = count
        game_power = reduce(lambda x, y: x * y, mins.values())
        total += game_power
    print(total)


if __name__ == "__main__":
    puzzle2()
