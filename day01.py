"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 1", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    dial = 50
    password = 0
    for line in lines:
        dial, _ = rotate_dial(dial, line)
        if dial == 0:
            password += 1
    return password

@runner("Day 1", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    dial = 50
    password = 0
    for line in lines:
        dial, hit_zero = rotate_dial(dial, line)
        password += hit_zero
    return password

def rotate_dial(loc: int, instruct: str) -> tuple[int,int]:
    """rotate the safe dial from current location based on instruction"""
    steps = int(instruct[1:])
    hit_zero = 0
    if steps > 100:
        cycles = steps // 100
        steps -= cycles * 100
        hit_zero = cycles
    if instruct[0] == "L":
        steps *= -1
    nloc = loc + steps
    if nloc > 99:
        nloc -= 100
        hit_zero += 1
    elif nloc < 0:
        nloc += 100
        if loc > 0:
            hit_zero += 1
    elif nloc == 0 and loc != 0:
        hit_zero += 1
    return nloc, hit_zero

# Data
data = read_lines("input/day01/input.txt")
sample = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()
sample2 = """R1000""".splitlines()

# Part 1
assert solve_part1(sample) == 3
assert solve_part1(data) == 1066

# Part 2
assert solve_part2(sample) == 6
assert solve_part2(sample2) == 10
assert solve_part2(data) == 6223
