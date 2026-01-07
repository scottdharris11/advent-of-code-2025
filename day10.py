"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 10", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    min_presses = 0
    for _, line in enumerate(lines):
        m = Machine(line)
        istates = set()
        istates.add(m.default_state())
        mip = min_init_presses(m, istates, 0, set())
        min_presses += mip
        #print(f"minimum presses for machine {i+1} of {len(lines)}: {mip}")
    return min_presses

@runner("Day 10", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    min_presses = 0
    for _, line in enumerate(lines):
        m = Machine(line)
        matrix = machine_to_matrix(m)
        free = []
        matrix = reduced_row_echelon(matrix, 0, 0, free)
        mip = min_joltage_presses(m, matrix, free, {})
        min_presses += mip
        #print(f"minimum presses for machine {i+1} of {len(lines)}: {mip}")
    return min_presses

class Button:
    """structure rerpesents a button"""
    def __init__(self, idx: int, s: str):
        self.idx = idx
        joltages = []
        for b in s[1:-1].split(','):
            joltages.append(int(b))
        self.joltages = tuple(joltages)

    def __repr__(self):
        return str((self.idx,self.joltages))

class Machine:
    """structure represents a machine"""
    def __init__(self, line: str):
        splits = line.split()
        init_pattern = []
        for s in splits[0][1:-1]:
            if s == '#':
                init_pattern.append(1)
            else:
                init_pattern.append(0)
        self.init_pattern = tuple(init_pattern)
        self.light_count = len(self.init_pattern)
        self.buttons = []
        for i, s in enumerate(splits[1:-1]):
            self.buttons.append(Button(i,s))
        joltage = []
        for j in splits[-1][1:-1].split(','):
            joltage.append(int(j))
        self.joltage = tuple(joltage)
        jtb = {}
        for i in range(len(self.joltage)):
            mapped = []
            for bi, b in enumerate(self.buttons):
                for ji in b.joltages:
                    if ji == i:
                        mapped.append(bi)
                        break
            jtb[i] = mapped
        self.joltage_to_buttons = jtb

    def __repr__(self):
        return str((self.light_count,self.init_pattern, self.buttons, self.joltage))

    def default_state(self) -> tuple[int]:
        """default light state for the machine"""
        state = [0] * self.light_count
        return tuple(state)

    def light_state(self, state: tuple[int], button: Button) -> tuple[int]:
        """light state after button applied"""
        output = list(state)
        for idx in button.joltages:
            output[idx] = (output[idx] + 1) % 2
        return tuple(output)

    def goal_init_state(self, state) -> bool:
        """determine if supplied state is the initialization state"""
        return state == self.init_pattern

    def click_range(self, button: Button, known: dict[int,int]) -> tuple[int,int]:
        """determine the click range for a button based on known previous clicks"""
        ja = list(self.joltage)
        for bi, bc in known.items():
            for j in self.buttons[bi].joltages:
                ja[j] -= bc
        minr, maxr = 0, None
        for ji in button.joltages:
            j = ja[ji]
            if maxr is None or j < maxr:
                maxr = j
            onlyone = True
            for b in self.joltage_to_buttons[ji]:
                if b != button.idx and b not in known:
                    onlyone = False
                    break
            if onlyone:
                minr = j
        return minr, maxr

    def valid_clicks(self, clicks: dict) -> bool:
        """determine if the supplied click amounts produce desired joltage"""
        for i, expected in enumerate(self.joltage):
            j = 0
            for b in self.joltage_to_buttons[i]:
                j += clicks[b]
            if j != expected:
                return False
        return True

def min_init_presses(m: Machine, states: set, presses: int, seen: set) -> int:
    """minimum number of button presses to reach machine initializaation state"""
    next_states = set()
    for state in states:
        for button in m.buttons:
            next_state = m.light_state(state, button)
            if m.goal_init_state(next_state):
                return presses + 1
            if next_state in seen:
                continue
            next_states.add(next_state)
            seen.add(next_state)
    return min_init_presses(m, next_states, presses+1, seen)

def machine_to_matrix(m: Machine) -> list[list[int]]:
    """build matrix of buttons/joltages for machine"""
    matrix = [[0] * (len(m.buttons) + 1) for _ in range(m.light_count)]
    for btn in m.buttons:
        for j in btn.joltages:
            matrix[j][btn.idx] = 1
    for i, j in enumerate(m.joltage):
        matrix[i][-1] = j
    return matrix

def reduced_row_echelon(m: list[list[int]], row: int, col: int, free: list[int]) -> list[list[int]]:
    """recursively adjust matrix until achieving reduced row echelon format"""
    # done when run out of rows or columns (extra columns when running out of rows are free)
    if row >= len(m) or col >= len(m[0]) - 1:
        for c in range(col, len(m[0]) - 1):
            free.append(c)
        return m

    # locate first row (at or below supplied row index) with 1 value in
    # supplied column.  If necessary swap that row with supplied index.
    # if none found, then skip that column (mark as free)
    prow = None
    for r in range(row, len(m)):
        if m[r][col] != 0:
            prow = r
            break
    if prow is None:
        free.append(col)
        return reduced_row_echelon(m, row, col+1, free)
    if prow > row:
        hold = m[row]
        m[row] = m[prow]
        m[prow] = hold

    # normalize the row values if the column value is not already "1"
    if m[row][col] != 1:
        adjust = 1 / m[row][col]
        for i, v in enumerate(m[row]):
            m[row][i] = m[row][i] * adjust

    # zero out row values in column before and after the row by
    # subtracting the current row from the row with the value
    current = m[row]
    for r, vals in enumerate(m):
        if r == row or vals[col] == 0:
            continue
        adjust = vals[col]
        for i, v in enumerate(vals):
            vals[i] = v - (current[i] * adjust)
    return reduced_row_echelon(m, row+1, col+1, free)

def min_joltage_presses(m: Machine, matrix: list[list[int]], free: list[int], clicks: dict) -> int:
    """minimum number of button presses to reach machine joltage state"""
    if len(free) == 0:
        filled = fill_clicks(matrix, clicks)
        if filled is not None and m.valid_clicks(filled):
            return sum(filled.values())
        return None
    minr, maxr = m.click_range(m.buttons[free[0]], clicks)
    mval = None
    for c in range(minr, maxr+1):
        clicks[free[0]] = c
        v = min_joltage_presses(m,matrix,free[1:],clicks)
        if v is not None and (mval is None or v < mval):
            mval = v
    clicks.pop(free[0],None)
    return mval

def fill_clicks(matrix: list[list[int]], known: dict[int,int]) -> dict[int,int]:
    """fill clicks until all equations are satisified"""
    clicks = {}
    clicks.update(known)
    changed = True
    while changed:
        changed = False
        for e in matrix:
            result = e[-1]
            notfilled = []
            for c, v in enumerate(e[:-1]):
                if v == 0:
                    continue
                if c in clicks:
                    result -= clicks[c] * v
                else:
                    notfilled.append(c)
            if len(notfilled) == 1:
                clicked = round(result * e[notfilled[0]])
                if clicked < 0:
                    return None
                clicks[notfilled[0]] = clicked
                changed = True
    return clicks

# Data
data = read_lines("input/day10/input.txt")
sample = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".splitlines()

# Part 1
assert solve_part1(sample) == 7
assert solve_part1(data) == 498

# Part 2
assert solve_part2(sample) == 33
assert solve_part2(data) == 17133
