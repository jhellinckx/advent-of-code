import math
from collections import defaultdict
from graphlib import TopologicalSorter


def read_input(filename="input.txt"):
    with open(filename) as f:
        after = defaultdict(set)
        while l := f.readline().strip():
            a, b = l.split("|")
            after[a].add(b)
        updates = []
        while l := f.readline().strip():
            updates.append(l.split(","))
    return after, updates


def check_order(pages, after):
    for i, page_number in enumerate(pages):
        for page_before in pages[:i]:
            if page_before in after[page_number]:
                return False
    return True


def puzzle1():
    after, updates = read_input()
    s = 0
    for pages in updates:
        if check_order(pages, after):
            s += int(pages[len(pages) // 2])
    print(s)


def puzzle2():
    after, updates = read_input()
    s = 0
    for pages in updates:
        if not check_order(pages, after):
            page_order = {page: i for i, page in enumerate(pages)}
            toporder = list(
                TopologicalSorter(
                    {
                        p: list(
                            sorted(
                                [a for a in after[p] if a in page_order],
                                key=lambda p: page_order[p],
                            )
                        )
                        for p in pages
                    }
                ).static_order()
            )
            s += int(toporder[len(toporder) // 2])
    return s


if __name__ == "__main__":
    print(puzzle2())
