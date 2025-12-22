"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 11", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    devices = parse_devices(lines)
    paths = []
    record_paths(devices, (), "you", paths)
    return len(paths)

@runner("Day 11", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    return 0

def record_paths(devices: dict, path: tuple, d: str, paths: list):
    """recursively find paths to output"""
    p = (*path, d)
    if d == "out":
        paths.append(p)
        return
    for n in devices.get(d,[]):
        record_paths(devices, p, n, paths)

def parse_devices(lines: list) -> dict[str,list[str]]:
    """parse devices from input"""
    devices = {}
    for line in lines:
        devices[line[0:3]] = line[5:].split()
    return devices

# Data
data = read_lines("input/day11/input.txt")
sample = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".splitlines()

# Part 1
assert solve_part1(sample) == 5
assert solve_part1(data) == 555

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
