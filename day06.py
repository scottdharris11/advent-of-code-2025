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
    equations = parse_equations(lines[-1])
    values = lines[:-1]
    total = 0
    for op, scol, ecol in equations:
        eq_vals = []
        for col in range(ecol,scol-1,-1):
            eq_vals.append([column_number(values,col)])
        if op == '+':
            total += add(eq_vals, 0)
        elif op == '*':
            total += multiply(eq_vals, 0)
    return total

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

def parse_equations(line: str) -> list[tuple[chr,int,int]]:
    """find the min/max of each equation column based on operator"""
    equations = []
    begin = 0
    for i, c in enumerate(line):
        if i > 0 and c in ['*','+']:
            equations.append((line[begin],begin,i-2))
            begin = i
    equations.append((line[begin],begin,len(line)-1))
    return equations

def column_number(values: list[str], col: int) -> int:
    """parse a number from a column"""
    s = ""
    for line in values:
        if line[col] != ' ':
            s += line[col]
    return int(s)

# Data
data = read_lines("input/day06/input.txt", False)
sample = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()

# Part 1
assert solve_part1(sample) == 4277556
assert solve_part1(data) == 6725216329103

# Part 2
assert solve_part2(sample) == 3263827
assert solve_part2(data) == 10600728112865
