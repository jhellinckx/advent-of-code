def get_history(filename="input.txt"):
    with open(filename, "r") as f:
        for line in f.readlines():
            yield list(map(int, line.strip().split(" ")))


def diffs(sequence):
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def get_sequences(input_sequence):
    sequences = [input_sequence]
    while not all(val == 0 for val in sequences[-1]):
        sequences.append(diffs(sequences[-1]))
    return sequences


def extrapolate(sequences):
    sequences[-1].append(0)
    for i in range(len(sequences) - 2, -1, -1):
        sequence = sequences[i]
        next_sequence = sequences[i + 1]
        sequence.append(sequence[-1] + next_sequence[-1])


def puzzle1():
    history = list(get_history("input.txt"))
    next_values = []
    for input_sequence in history:
        sequences = get_sequences(input_sequence)
        extrapolate(sequences)
        next_values.append(sequences[0][-1])
    print(sum(next_values))


def extrapolate_backwards(sequences):
    sequences[-1].insert(0, 0)
    for i in range(len(sequences) - 2, -1, -1):
        sequence = sequences[i]
        next_sequence = sequences[i + 1]
        sequence.insert(0, sequence[0] - next_sequence[0])


def puzzle2():
    history = list(get_history("input.txt"))
    previous_values = []
    for input_sequence in history:
        sequences = get_sequences(input_sequence)
        extrapolate_backwards(sequences)
        previous_values.append(sequences[0][0])
    print(sum(previous_values))


if __name__ == "__main__":
    puzzle2()
