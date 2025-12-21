"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 10", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    min_presses = 0
    for _, line in enumerate(lines):
        m = Machine(line)
        mip = min_init_presses(m, [(None, [0]*m.light_count)], 0)
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
        self.init_pattern = []
        for s in splits[0][1:-1]:
            if s == '#':
                self.init_pattern.append(1)
            else:
                self.init_pattern.append(0)
        self.light_count = len(self.init_pattern)
        self.buttons = []
        for s in splits[1:-1]:
            button = []
            for b in s[1:-1].split(','):
                button.append(int(b))
            self.buttons.append(button)
        self.joltage = []
        for j in splits[-1][1:-1].split(','):
            self.joltage.append(int(j))

    def __repr__(self):
        return str((self.light_count,self.init_pattern, self.buttons, self.joltage))

    def light_state(self, current: list[int], button: list[int]) -> list[int]:
        """light state after button applied"""
        output = current[:]
        for idx in button:
            output[idx] = (output[idx] + 1) % 2
        return output

    def goal_state(self, state) -> bool:
        """determine if supplied state is the initialization state"""
        return state == self.init_pattern

def min_init_presses(m: Machine, states: list, presses: int) -> int:
    """minimum number of button presses to reach machine initializaation state"""
    next_states = []
    for last_button, state in states:
        for button in m.buttons:
            if last_button == button:
                continue
            next_state = m.light_state(state, button)
            if m.goal_state(next_state):
                return presses + 1
            next_states.append((button,next_state))
    return min_init_presses(m, next_states, presses+1)

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
