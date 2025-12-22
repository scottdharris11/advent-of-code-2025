"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 12", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    return 0
# Data
data = read_lines("input/day12/input.txt")
sample = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2""".splitlines()

# Part 1
assert solve_part1(sample) == 0
assert solve_part1(data) == 0
