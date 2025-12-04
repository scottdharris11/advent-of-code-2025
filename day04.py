"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 4", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    accessible = 0
    depth = len(lines)
    width = len(lines[0])
    for y, line in enumerate(lines):
        for x, loc in enumerate(line):
            if loc == '@' and can_access(lines, width, depth, x, y):
                accessible += 1
    return accessible

@runner("Day 4", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    return 0

def can_access(grid: list[str], w: int, d: int, x: int, y: int) -> bool:
    """determine if location can be accessed"""
    blocking = 0
    for ox, oy in [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]:
        nx = x + ox
        ny = y + oy
        if nx < 0 or nx >= w or ny < 0 or ny >= d:
            continue
        if grid[ny][nx] == '@':
            blocking += 1
    return blocking < 4

# Data
data = read_lines("input/day04/input.txt")
sample = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()

# Part 1
assert solve_part1(sample) == 13
assert solve_part1(data) == 1419

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
