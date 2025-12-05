"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 5", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    fresh_ranges, ingredients = parse_input(lines)
    fresh = 0
    for i in ingredients:
        for minr, maxr in fresh_ranges:
            if minr <= i <= maxr:
                fresh += 1
                break
    return fresh

@runner("Day 5", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    return 0

def parse_input(lines: list) -> tuple[list,list]:
    """parse input into workable structures"""
    idx = 0
    fresh_ranges = []
    while lines[idx] != "":
        a, b = lines[idx].split("-")
        fresh_ranges.append((int(a),int(b)))
        idx += 1
    ingredients = []
    for line in lines[idx+1:]:
        ingredients.append(int(line))
    return fresh_ranges, ingredients

# Data
data = read_lines("input/day05/input.txt")
sample = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()

# Part 1
assert solve_part1(sample) == 3
assert solve_part1(data) == 707

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
