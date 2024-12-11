def read_input(filename="input.txt"):
    with open(filename) as f:
        dense_disk_map = f.readline().strip()
    file_blocks = []
    free_spaces = []
    for i, v in enumerate(dense_disk_map):
        if i % 2 == 0:
            file_blocks.append([(i // 2, int(v))])
        else:
            file_blocks.append([])
            free_spaces.append((i, int(v)))
    return file_blocks, free_spaces


def last_file_index(file_blocks):
    for i in range(len(file_blocks) - 1, -1, -1):
        if file_blocks[i]:
            return i


def checksum(file_blocks):
    i = 0
    s = 0
    for blocks in file_blocks:
        for block in blocks:
            if block:
                file_id = block[0]
                for _ in range(block[1]):
                    if file_id != -1:
                        s += file_id * i
                    i += 1
    return s


def puzzle1():
    file_blocks, free_spaces = read_input()
    file_index = None
    while free_spaces:
        space_index, space_size = free_spaces.pop(0)
        while space_size:
            if not file_index:
                file_index = last_file_index(file_blocks)
            file_id, file_size = file_blocks[file_index][0]
            if file_size > space_size:
                file_blocks[file_index][0] = (file_id, file_size - space_size)
                file_blocks[space_index].append((file_id, space_size))
                space_size = 0
            else:
                file_blocks[file_index] = []
                file_blocks[space_index].append((file_id, file_size))
                space_size -= file_size
                file_index = None
                if free_spaces:
                    free_spaces.pop()

    return checksum(file_blocks)


def puzzle2():
    file_blocks, free_spaces = read_input()
    for file_index in range(len(file_blocks) - 1, -1, -1):
        if file_blocks[file_index]:
            file_id, file_size = file_blocks[file_index][0]
            for j, (space_index, space_size) in enumerate(free_spaces):
                if space_index >= file_index:
                    break
                if space_size >= file_size:
                    file_blocks[space_index].append((file_id, file_size))
                    file_blocks[file_index] = []
                    free_spaces[j] = (space_index, space_size - file_size)
                    free_spaces.append((file_index, file_size))
                    break
    for space_index, space_size in free_spaces:
        if space_size:
            file_blocks[space_index].append((-1, space_size))
    return checksum(file_blocks)


if __name__ == "__main__":
    print(puzzle2())
