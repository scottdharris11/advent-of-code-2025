"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 7", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    start_x = lines[0].index("S")
    beams = set()
    beams.add(start_x)
    splits = 0
    for y in range(2,len(lines)):
        nbeams = set()
        for beam in beams:
            if lines[y][beam] == '^':
                splits += 1
                nbeams.add(beam-1)
                nbeams.add(beam+1)
            else:
                nbeams.add(beam)
        beams = nbeams
    return splits

@runner("Day 7", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    start_x = lines[0].index("S")
    beams = {start_x:1}
    for y in range(2,len(lines)):
        nbeams = {}
        for beam, count in beams.items():
            if lines[y][beam] == '^':
                nbeams[beam-1] = nbeams.get(beam-1,0) + count
                nbeams[beam+1] = nbeams.get(beam+1,0) + count
            else:
                nbeams[beam] = nbeams.get(beam,0) + count
        beams = nbeams
    return sum(beams.values())

# Data
data = read_lines("input/day07/input.txt")
sample = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".splitlines()

# Part 1
assert solve_part1(sample) == 21
assert solve_part1(data) == 1499

# Part 2
assert solve_part2(sample) == 40
assert solve_part2(data) == 24743903847942
