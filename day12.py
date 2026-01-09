"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 12", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    presents, regions = parse_input(lines)
    possible = 0
    not_possible = 0
    for region in regions:
        if region.fit_no_manipulation(presents):
            possible += 1
        elif region.not_possible(presents):
            not_possible += 1
    #print(f"regions: {len(regions)}, not possibe: {not_possible}, possible w/o manip: {possible}")
    return possible

class Present:
    """represents the structure of Present"""
    def __init__(self, lines: list[str]):
        self.shapes = []
        self.size = 0
        self.box_size = 0
        for line in lines:
            for c in line:
                if c == '#':
                    self.size += 1
            self.box_size = max(self.box_size, len(line))
        self.box_size *= len(lines)

    def size_required(self, count: int) -> int:
        """determine the mininum number of grids required to hold number of presents"""
        return count * self.size

    def box_size_required(self, count: int) -> int:
        """determine the minimum size needed with no manipulation of space"""
        return count * self.box_size

class Region:
    """represents the struture of Region to hold presents"""
    def __init__(self, line: str):
        splits = line.split()
        size = splits[0].split("x")
        self.width = int(size[0])
        self.height = int(size[1][:-1])
        self.total_size = self.width * self.height
        self.counts = [int(c) for c in splits[1:]]

    def fit_no_manipulation(self, presents: list[Present]) -> bool:
        """determine if region will just work without any maninpulation"""
        ts = 0
        for i, c in enumerate(self.counts):
            ts += presents[i].box_size_required(c)
        return ts <= self.total_size

    def not_possible(self, presents: list[Present]) -> bool:
        """determine if region will never work regardless of manipulation"""
        ts = 0
        for i, c in enumerate(self.counts):
            ts += presents[i].size_required(c)
        return ts > self.total_size

def parse_input(lines: list[str]) -> tuple[list[Present], list[Region]]:
    """parse input into working structures"""
    presents = []
    for s in range(0,26,5):
        presents.append(Present(lines[s+1:s+4]))
    regions = [Region(r) for r in lines[30:]]
    return presents, regions

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
#assert solve_part1(sample) == 2
assert solve_part1(data) == 517
