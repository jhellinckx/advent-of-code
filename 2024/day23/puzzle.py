from collections import defaultdict


def read_input(filename="input.txt"):
    g = defaultdict(set)
    with open(filename) as f:
        for line in f.readlines():
            l, r = line.strip().split("-")
            g[l].add(r)
            g[r].add(l)
    return g


def bron_kerbosch(r, p, x, g, max_cliques):
    if not p and not x:
        max_cliques.append(r)
    for v in list(p):
        bron_kerbosch(
            r.union({v}), p.intersection(g[v]), x.intersection(g[v]), g, max_cliques
        )
        p.remove(v)
        x.add(v)


def puzzle1():
    g = read_input()
    inter_conn = set()
    for c, adj in g.items():
        if not c.startswith("t"):
            continue
        for a in adj:
            for b in g[a]:
                if b in adj:
                    inter_conn.add(tuple(sorted((c, a, b))))
    return len(inter_conn)


def puzzle2():
    g = read_input()
    max_cliques = []
    bron_kerbosch(set(), set(g.keys()), set(), g, max_cliques)
    max_clique = sorted(max_cliques, key=len, reverse=True)[0]
    return ",".join(sorted(max_clique))


if __name__ == "__main__":
    print(puzzle1())
