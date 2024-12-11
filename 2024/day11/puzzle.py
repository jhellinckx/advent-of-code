from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [int(n) for n in f.readline().strip().split(" ")]


def count_stones(stones, blinks):
    stones = {stone: 1 for stone in stones}
    for _ in range(blinks):
        next_stones = defaultdict(int)
        for stone, n in stones.items():
            if stone == 0:
                next_stones[1] += n
            elif len(stone_str := str(stone)) % 2 == 0:
                next_stones[int(stone_str[: len(stone_str) // 2])] += n
                next_stones[int(stone_str[len(stone_str) // 2 :])] += n
            else:
                next_stones[stone * 2024] += n
        stones = next_stones
    return sum(stones.values())


def puzzle1():
    stones = read_input()
    return count_stones(stones, 25)


def puzzle2():
    stones = read_input()
    return count_stones(stones, 75)


if __name__ == "__main__":
    print(puzzle2())
