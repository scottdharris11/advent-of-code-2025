"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 6", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    values, operators = parse_input(lines)
    equations = len(values[0])
    total = 0
    for i in range(equations):
        if operators[i] == '+':
            total += add(values, i)
        elif operators[i] == '*':
            total += multiply(values, i)
    return total

@runner("Day 6", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    return 0

def add(values: list[list[int]], column: int) -> int:
    """add the values in the supplied list column"""
    result = 0
    for row in values:
        result += row[column]
    return result

def multiply(values: list[list[int]], column: int) -> int:
    """multiply the values in the supplied list column"""
    result = 1
    for row in values:
        result *= row[column]
    return result

def parse_input(lines: list) -> tuple[list[list[int]],list[chr]]:
    """parse the input into list of integers and list of operators"""
    values = []
    for line in lines:
        if line[0] == '+' or line[0] == '*':
            break
        values.append([int(v) for v in line.split()])
    operators = list(lines[-1].split())
    return values, operators

# Data
data = read_lines("input/day06/input.txt")
sample = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()

# Part 1
assert solve_part1(sample) == 4277556
assert solve_part1(data) == 6725216329103

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
