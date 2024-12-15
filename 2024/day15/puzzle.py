import re


def replace_all(s, replace):
    for k, v in replace.items():
        s = s.replace(k, v)
    return s


def read_input(filename="input.txt", replace={"#": "#", ".": ".", "O": "O", "@": "@"}):
    with open(filename) as f:
        content = f.read()
        m = [
            list(replace_all(l.strip(), replace))
            for l in re.findall(r"[#.O@]+\n", content)
        ]
        moves = re.findall(r"[\^<>v]", content)
        return m, moves


def find_robot(m):
    for i, row in enumerate(m):
        for j, c in enumerate(row):
            if c == "@":
                return i, j


def move_robot_1(m, move, i, j):
    di, dj = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }[move]
    ii, jj = i + di, j + dj
    pushed_box = False
    while m[ii][jj] == "O":
        pushed_box = True
        ii, jj = ii + di, jj + dj
    if m[ii][jj] == "#":
        return i, j
    if m[ii][jj] == ".":
        if pushed_box:
            m[ii][jj] = "O"
        m[i][j] = "."
        m[i + di][j + dj] = "@"
        return i + di, j + dj


def puzzle1():
    m, moves = read_input()
    robot = find_robot(m)
    for move in moves:
        robot = move_robot_1(m, move, *robot)
    return sum(
        100 * i + j for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == "O"
    )


def move_robot_2(m, move, i, j):
    di, dj = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }[move]
    ii, jj = i + di, j + dj
    if m[ii][jj] == "#":
        return i, j
    if m[ii][jj] == ".":
        m[i][j] = "."
        m[ii][jj] = "@"
        return ii, jj
    if move in "<>" and m[ii][jj] in "[]":
        ii, jj = ii + di, jj + dj
        while m[ii][jj] in "[]":
            ii, jj = ii + di, jj + dj
        if m[ii][jj] == "#":
            return i, j
        if m[ii][jj] == ".":
            ii, jj = ii - di, jj - dj
            while m[ii][jj] in "[]":
                m[ii + di][jj + dj] = m[ii][jj]
                ii, jj = ii - di, jj - dj
            m[i + di][j + dj] = "@"
            m[i][j] = "."
            return i + di, j + dj

    def box_at(i, j):
        return (i, j) if m[i][j] == "[" else (i, j - 1)

    if move in "^v" and m[ii][jj] in "[]":
        bi, bj = box_at(ii, jj)
        moved_boxes = {(bi, bj)}
        all_boxes = []
        while moved_boxes:
            next_boxes = set()
            for bi, bj in moved_boxes:
                for bii, bjj in [(bi + di, bj + dj), (bi + di, bj + dj + 1)]:
                    if m[bii][bjj] == "#":
                        return i, j
                    if m[bii][bjj] in "[]":
                        next_boxes.add(box_at(bii, bjj))
            all_boxes.append(moved_boxes)
            moved_boxes = next_boxes
        for boxes in all_boxes[::-1]:
            for bi, bj in boxes:
                m[bi + di][bj + dj] = "["
                m[bi + di][bj + dj + 1] = "]"
                m[bi][bj] = "."
                m[bi][bj + 1] = "."
        m[i + di][j + dj] = "@"
        m[i][j] = "."
        return i + di, j + dj
    return i, j


def puzzle2():
    m, moves = read_input(replace={"#": "##", ".": "..", "O": "[]", "@": "@."})
    robot = find_robot(m)
    for move in moves:
        robot = move_robot_2(m, move, *robot)
    return sum(
        100 * i + j for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == "["
    )


if __name__ == "__main__":
    print(puzzle2())
