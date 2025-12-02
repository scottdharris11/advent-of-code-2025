"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 2", "Part 1")
def solve_part1(line: str) -> int:
    """part 1 solving function"""
    invalid_sum = 0
    for r in line.split(","):
        s = r.split("-")
        minr = int(s[0])
        maxr = int(s[1])
        for i in range(minr, maxr+1):
            if not valid_id_simple(i):
                invalid_sum += i
    return invalid_sum

@runner("Day 2", "Part 2")
def solve_part2(line: str) -> int:
    """part 2 solving function"""
    invalid_sum = 0
    for r in line.split(","):
        s = r.split("-")
        minr = int(s[0])
        maxr = int(s[1])
        for i in range(minr, maxr+1):
            if not valid_id_complex(i):
                invalid_sum += i
    return invalid_sum

def valid_id_simple(i: int) -> bool:
    """determine if the supplied id is valid"""
    s = str(i)
    l = len(s)
    if l % 2 != 0:
        return True
    l = l // 2
    return s[:l] != s[l:]

def valid_id_complex(i: int) -> bool:
    """determine if the supplied id is valid"""
    s = str(i)
    l = len(s)
    half = l // 2
    # cycle the potential character count ranges from 1 up to half
    # of the number length.  if the character count doesn't evenly
    # line up with the string length, skip that count, otherwise
    # compare each segment.  invalid if find a segment count that
    # matches all segments of the string
    for c in range(1,half+1):
        if l % c != 0:
            continue
        cntl = s[:c]
        all_matched = True
        for idx in range(c,l-c+1,c):
            if cntl != s[idx:idx+c]:
                all_matched = False
                break
        if all_matched:
            return False
    return True

# Data
data = read_lines("input/day02/input.txt")[0]
sample = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""".splitlines()[0]

# Part 1
assert solve_part1(sample) == 1227775554
assert solve_part1(data) == 38437576669

# Part 2
assert solve_part2(sample) == 4174379265
assert solve_part2(data) == 49046150754
