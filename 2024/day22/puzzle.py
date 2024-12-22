from collections import Counter
from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename) as f:
        return [int(l.strip()) for l in f.readlines()]


def all_secret_xors(k):
    s = [[f"{i:02}"] for i in range(24)]
    secrets = []
    for _ in range(k):
        s1 = [s[i] + s[i + 6] for i in range(18)] + s[18:]
        s2 = s1[:5] + [s1[i] + s1[i - 5] for i in range(5, 24)]
        s3 = [s2[i] + s2[i + 11] for i in range(13)] + s2[13:]
        s = []
        for b in s3:
            counter = Counter(b)
            for v, c in counter.items():
                if c % 2 == 0:
                    b = [i for i in b if i != v]
                else:
                    b = [i for i in b if i != v] + [v]
            s.append(sorted(b))
        secrets.append([[int(i) for i in b] for b in s])
    return secrets


secret_xors = all_secret_xors(2000)


def find_secret(s, k):
    s_bits = [int(i) for i in f"{s:024b}"]
    new_s = []
    for xors in secret_xors[k - 1]:
        bit = s_bits[xors[0]]
        for j in range(1, len(xors)):
            bit ^= s_bits[xors[j]]
        new_s.append(str(bit))
    return int("".join(new_s), 2)


def find_all_secrets(s, k):
    return [find_secret(s, i) for i in range(1, k + 1)]


def puzzle1():
    return sum(find_secret(s, 2000) for s in read_input())


def puzzle2():
    price_changes_profits = defaultdict(int)
    for first_secret in read_input():
        changes = {}
        last_digits = {}
        secrets = [first_secret] + find_all_secrets(first_secret, 2000)
        changes_seen = set()
        for i, secret in enumerate(secrets):
            last_digit = int(str(secret)[-1])
            last_digits[i] = last_digit
            if i == 0:
                continue
            changes[i] = last_digit - last_digits[i - 1]
            if i < 4:
                continue
            changes_key = (changes[i - 3], changes[i - 2], changes[i - 1], changes[i])
            if changes_key not in changes_seen:
                changes_seen.add(changes_key)
                price_changes_profits[changes_key] += last_digit
    return max(price_changes_profits.values())


if __name__ == "__main__":
    print(puzzle2())
