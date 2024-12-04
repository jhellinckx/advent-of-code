from collections import Counter


def get_hands(filename="input.txt"):
    with open(filename, "r") as f:
        while line := f.readline():
            hand, bet = line.strip().split(" ")
            yield hand, int(bet)


card_values = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,  # remove for puzzle1
}

candidates = list(card_values.copy().keys())
candidates.remove("J")


def hand_score(hand, init_cards=None):
    hand = hand[0]
    if not init_cards:
        init_cards = hand
    counts = Counter(hand)
    score = sum(map(lambda c: 10 ** (c - 1), counts.values()))
    return (score, *list(map(lambda c: card_values[c], list(init_cards))))


def get_winnings(hands):
    winnings = 0
    for i, (hand, bet) in enumerate(hands):
        rank = i + 1
        winnings += rank * bet
    return winnings


def puzzle1():
    hands = get_hands()
    hands = sorted(hands, key=hand_score)
    print(get_winnings(hands))


def max_score(hand, init_cards=None):
    cards, bet = hand
    if (i := cards.find("J")) < 0:
        return hand_score(hand, init_cards)
    scores = []
    for c in candidates:
        scores.append(
            max_score((cards[:i] + c + cards[i + 1 :], bet), init_cards or cards)
        )
    return max(scores)


def puzzle2():
    hands = get_hands()
    hands = sorted(hands, key=max_score)
    print(get_winnings(hands))


if __name__ == "__main__":
    puzzle2()
