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
    return 0

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
        for s in splits[1:-1]:
            button = []
            for b in s[1:-1].split(','):
                button.append(int(b))
            self.buttons.append(tuple(button))
        self.joltage = []
        for j in splits[-1][1:-1].split(','):
            self.joltage.append(int(j))

    def __repr__(self):
        return str((self.light_count,self.init_pattern, self.buttons, self.joltage))

    def default_state(self) -> tuple[int]:
        """default light state for the machine"""
        state = [0] * self.light_count
        return tuple(state)

    def light_state(self, state: tuple[int], button: tuple[int]) -> tuple[int]:
        """light state after button applied"""
        output = list(state)
        for idx in button:
            output[idx] = (output[idx] + 1) % 2
        return tuple(output)

    def goal_state(self, state) -> bool:
        """determine if supplied state is the initialization state"""
        return state == self.init_pattern

def min_init_presses(m: Machine, states: set, presses: int, seen: set) -> int:
    """minimum number of button presses to reach machine initializaation state"""
    next_states = set()
    for state in states:
        for button in m.buttons:
            next_state = m.light_state(state, button)
            if m.goal_state(next_state):
                return presses + 1
            if next_state in seen:
                continue
            next_states.add(next_state)
            seen.add(next_state)
    return min_init_presses(m, next_states, presses+1, seen)

# Data
data = read_lines("input/day10/input.txt")
sample = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".splitlines()

# Part 1
assert solve_part1(sample) == 7
assert solve_part1(data) == 498

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
