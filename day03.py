"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 3", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    jolts = 0
    for line in lines:
        jolts += max_joltage(line)
    return jolts

@runner("Day 3", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    return 0

def max_joltage(batts: str) -> int:
    """determine max joltage for battery bank"""
    fidx = 0
    fval = 0
    for i, batt in enumerate(batts[:-1]):
        j = int(batt)
        if j > fval:
            fval = j
            fidx = i
    sval = 0
    for batt in batts[fidx+1:]:
        j = int(batt)
        if j > sval:
            sval = j
    return (fval * 10) + sval

# Data
data = read_lines("input/day03/input.txt")
sample = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

# Part 1
assert solve_part1(sample) == 357
assert solve_part1(data) == 16993

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
