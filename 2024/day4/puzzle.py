import re

from functools import reduce


def read_input(target_word, filename="input.txt"):
    with open(filename) as f:
        return [
            [c if c in target_word else "." for c in l.strip()] for l in f.readlines()
        ]


def puzzle1():
    target_word = "XMAS"
    word_search = read_input(target_word=target_word)
    matches = 0
    size_v, size_h = len(word_search), len(word_search[0])
    directions = [(di, dj) for di in range(-1, 2) for dj in range(-1, 2) if di or dj]
    for i in range(size_v):
        for j in range(size_h):
            if word_search[i][j] == target_word[0]:
                for di, dj in directions:
                    match = True
                    for k in range(1, len(target_word)):
                        ii = i + di * k
                        jj = j + dj * k
                        if not (0 <= ii < size_v and 0 <= jj < size_h):
                            match = False
                            break
                        if word_search[ii][jj] != target_word[k]:
                            match = False
                            break
                    if match:
                        matches += 1
    return matches


def puzzle2():
    target_word = "MAS"
    trigger_search = "A"
    word_search = read_input(target_word=target_word)
    matches = 0
    size_v, size_h = len(word_search), len(word_search[0])
    directions = [[(1, 1), (0, 0), (-1, -1)], [(1, -1), (0, 0), (-1, 1)]]

    def in_bounds(i, j):
        return 0 <= i < size_v and 0 <= j < size_h

    for i in range(size_v):
        for j in range(size_h):
            if word_search[i][j] == trigger_search:
                words = [
                    "".join(
                        word_search[i + di][j + dj]
                        for di, dj in w
                        if in_bounds(i + di, j + dj)
                    )
                    for w in directions
                ]
                matches += int(
                    all(w == target_word or w == target_word[::-1] for w in words)
                )
    return matches


if __name__ == "__main__":
    print(puzzle2())
