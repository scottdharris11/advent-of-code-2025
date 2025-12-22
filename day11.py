"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 11", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    devices = parse_devices(lines)
    paths = []
    record_paths(devices, (), "you", "out", paths)
    return len(paths)

@runner("Day 11", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    devices = parse_devices(lines)
    _, _, _, both = count_paths_to(devices, "svr", "out", {})
    return both

def record_paths(devices: dict, path: tuple, d: str, goal: str, paths: list):
    """recursively find paths to output"""
    p = (*path, d)
    if d == goal:
        paths.append(p)
        return
    for n in devices.get(d,[]):
        if n not in p:
            record_paths(devices, p, n, goal, paths)

def count_paths_to(devices: dict, device: str, goal: str, cache: dict) -> tuple[int]:
    """recursively find paths to output"""
    if device in cache:
        return cache[device]
    paths = 0
    paths_with_fft = 0
    paths_with_dac = 0
    paths_with_both = 0
    for n in devices.get(device,[]):
        if n == goal:
            paths += 1
        else:
            p, fc, dc, bc = count_paths_to(devices, n, goal, cache)
            paths += p
            paths_with_fft += fc
            paths_with_dac += dc
            paths_with_both += bc
            if n == "fft":
                paths_with_fft += p
                paths_with_both += dc
            elif n == "dac":
                paths_with_dac += p
                paths_with_both += fc
    results = (paths, paths_with_fft, paths_with_dac, paths_with_both)
    cache[device] = results
    return results

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
sample2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""".splitlines()

# Part 1
assert solve_part1(sample) == 5
assert solve_part1(data) == 555

# Part 2
assert solve_part2(sample2) == 2
assert solve_part2(data) == 502447498690860
