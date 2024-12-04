def get_cards(filename="input.txt"):
    with open(filename, "r") as f:
        for line in f.readlines():
            winning, numbers = line.split(":")[1].split("|")
            winning = list(filter(str.isdigit, map(str.strip, winning.split(" "))))
            numbers = list(filter(str.isdigit, map(str.strip, numbers.split(" "))))
            yield set(winning), numbers


def count_matches(winning, numbers):
    return sum(map(lambda number: int(number in winning), numbers))


def puzzle1():
    cards = get_cards()
    all_points = []
    for winning, numbers in cards:
        matches = count_matches(winning, numbers)
        if matches > 0:
            all_points.append(2 ** (matches - 1))

    print(sum(all_points))


def puzzle2():
    cards = list(get_cards())
    matches_cache = {}
    queue = list(range(len(cards)))
    total = 0
    while queue:
        i = queue.pop()
        total += 1
        if i not in matches_cache:
            matches_cache[i] = count_matches(*cards[i])
        matches = matches_cache[i]
        if matches:
            queue += list(range(i + 1, i + 1 + matches))
    print(total)


if __name__ == "__main__":
    puzzle2()
