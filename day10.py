"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 10", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    return 0

@runner("Day 10", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    return 0

# Data
data = read_lines("input/day10/input.txt")
sample = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".splitlines()

# Part 1
assert solve_part1(sample) == 7
assert solve_part1(data) == 0

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
