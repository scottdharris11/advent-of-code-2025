"""utility imports"""
from math import sqrt
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 8", "Part 1")
def solve_part1(lines: list, connections: int) -> int:
    """part 1 solving function"""
    boxes = parse_boxes(lines)

    # calculate distances between unique box combinations
    distances = []
    for i, a in enumerate(boxes):
        for b in boxes[i+1:]:
            d = distance_between(a,b)
            distances.append((d,a,b))
    distances.sort(key=lambda d: d[0])

    # connect desired number of boxes, establishing circuts
    circuits = []
    circuits_by_box = {}
    for _, a, b in distances[:connections]:
        ac = circuits_by_box.get(a, None)
        bc = circuits_by_box.get(b, None)
        if ac is not None and bc is not None:
            if ac == bc:
                # already in same circuit, just skip
                pass
            else:
                # joining existing circuits
                ac.extend(bc)
                for box in bc:
                    circuits_by_box[box] = ac
                circuits.remove(bc)
        elif ac is not None:
            ac.append(b)
            circuits_by_box[b] = ac
        elif bc is not None:
            bc.append(a)
            circuits_by_box[a] = bc
        else:
            # new cicuit
            circuit = [a, b]
            circuits.append(circuit)
            circuits_by_box[a] = circuit
            circuits_by_box[b] = circuit

    # build result off the length of 3 largest circuits
    circuits.sort(key=len, reverse=True)
    result = 1
    for c in circuits[:3]:
        result *= len(c)
    return result

@runner("Day 8", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    return 0

def distance_between(a: tuple[int,int,int], b: tuple[int,int,int]) -> float:
    """calculate the straight line distance between two junction boxes"""
    ax, ay, az = a
    bx, by, bz = b
    return sqrt((ax-bx)**2 + (ay-by)**2 + (az-bz)**2)

def parse_boxes(lines: list[str]) -> list[tuple[int,int,int]]:
    """parse junction boxes from input"""
    boxes = []
    for line in lines:
        x,y,z = line.split(",")
        boxes.append(((int(x),int(y),int(z))))
    return boxes

# Data
data = read_lines("input/day08/input.txt")
sample = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".splitlines()

# Part 1
assert solve_part1(sample, 10) == 40
assert solve_part1(data, 1000) == 140008

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
