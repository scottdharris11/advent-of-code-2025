"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 9", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    tiles = parse_tiles(lines)
    max_area = 0
    for i, a in enumerate(tiles):
        for b in tiles[i+1:]:
            t = area(a,b)
            max_area = max(max_area, t)
    return max_area

@runner("Day 9", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    return 0

def area(a: tuple[int,int], b: tuple[int,int]) -> int:
    """calculate the area between the two tiles when recentangle formed"""
    ax, ay = a
    bx, by = b
    return (abs(ax-bx)+1) * (abs(ay-by)+1)

def parse_tiles(lines: list[str]) -> list[tuple[int,int]]:
    """parse junction boxes from input"""
    tiles = []
    for line in lines:
        x,y = line.split(",")
        tiles.append(((int(x),int(y))))
    return tiles

# Data
data = read_lines("input/day09/input.txt")
sample = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()

# Part 1
assert solve_part1(sample) == 50
assert solve_part1(data) == 4729332959

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
