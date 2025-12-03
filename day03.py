"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 3", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    jolts = 0
    for line in lines:
        jolts += max_joltage(line, 0, 2, "")
    return jolts

@runner("Day 3", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    jolts = 0
    for line in lines:
        jolts += max_joltage(line, 0, 12, "")
    return jolts

def max_joltage(batts: str, sidx: int, left: int, jolts: str) -> int:
    """determine max joltage for battery bank"""
    if left == 0:
        return int(jolts)
    midx = 0
    mval = 0
    for i, batt in enumerate(batts[sidx:len(batts)-left+1]):
        j = int(batt)
        if j > mval:
            mval = j
            midx = i + sidx
    jolts += batts[midx]
    return max_joltage(batts, midx+1, left-1, jolts)

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
assert solve_part2(sample) == 3121910778619
assert solve_part2(data) == 168617068915447
