def get_maps(filename="input.txt"):
    maps = {}
    seeds = []
    with open(filename, "r") as f:
        seeds = f.readline().split(":")[1].strip().split(" ")
        seeds = list(map(int, map(str.strip, seeds)))
        while line := f.readline():
            line = line.strip()
            if line.endswith("map:"):
                ranges = []
                source, dest = line.split(" ")[0].split("-to-")
                while line := f.readline().strip():
                    dest_start, source_start, length = list(map(int, line.split(" ")))
                    ranges.append((source_start, dest_start, length))
                maps[source] = {"dest": dest, "ranges": ranges}

    return seeds, maps


def find_location(seed, maps):
    source = "seed"
    number = seed
    while source != "location":
        dest = maps[source]["dest"]
        ranges = maps[source]["ranges"]
        for source_start, dest_start, length in ranges:
            if source_start <= number < source_start + length:
                number = dest_start + (number - source_start)
                source = dest
                break
            source = dest
    return number


def puzzle1():
    seeds, maps = get_maps()
    location_numbers = []
    for seed in seeds:
        location_numbers.append(find_location(seed, maps))
    print(min(location_numbers))


def puzzle2():
    seeds, maps = get_maps("input.txt")
    ranges_queue = [("seed", seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    location_numbers = []
    while ranges_queue:
        source, source_start, length = ranges_queue.pop()
        if source == "location":
            location_numbers.append(source_start)
            continue
        dest = maps[source]["dest"]
        ranges = maps[source]["ranges"]
        match = False
        for map_source_start, map_dest_start, map_length in ranges:
            if source_start < map_source_start < source_start + length:
                # CUT BEFORE
                matched_length = min(
                    (source_start + length) - map_source_start, map_length
                )
                ranges_queue.append((dest, map_dest_start, matched_length))
                length = length - matched_length
            if map_source_start <= source_start < map_source_start + map_length:
                match = True
                dest_start = map_dest_start + (source_start - map_source_start)
                if map_source_start + map_length >= source_start + length:
                    # FULLY INSIDE
                    ranges_queue.append((dest, dest_start, length))
                    break
                else:
                    # CUT AFTER
                    matched_length = (map_source_start + map_length) - source_start
                    ranges_queue.append((dest, dest_start, matched_length))
                    ranges_queue.append(
                        (source, map_source_start + map_length, length - matched_length)
                    )
                    break
        if not match:
            ranges_queue.append((dest, source_start, length))
    print(min(location_numbers))


if __name__ == "__main__":
    puzzle2()
