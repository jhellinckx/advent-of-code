import math


def get_nodes(filename="input.txt"):
    with open(filename, "r") as f:
        instructions = [0 if i == "L" else 1 for i in f.readline().strip()]
        f.readline()
        nodes = {}
        for line in f.readlines():
            src, dest = line.strip().split(" = ")
            l, r = dest.strip("()").split(", ")
            nodes[src] = (l, r)
    return instructions, nodes


def puzzle1(start="AAA", end="ZZZ"):
    instructions, nodes = get_nodes()
    found = False
    node = start
    i = 0
    steps = 0
    while not found:
        node = nodes[node][instructions[i]]
        steps += 1
        i += 1
        i %= len(instructions)
        if node == end:
            found = True
    print(steps)


def puzzle2():
    instructions, nodes = get_nodes("input.txt")
    current_nodes = [node for node in nodes if node.endswith("A")]
    all_steps = []
    for node in current_nodes:
        found = False
        i = 0
        steps = 0
        while not found:
            node = nodes[node][instructions[i]]
            steps += 1
            i += 1
            i %= len(instructions)
            if node.endswith("Z"):
                found = True
        all_steps.append(steps)
    print(all_steps)
    print(math.lcm(*all_steps))


if __name__ == "__main__":
    puzzle2()
