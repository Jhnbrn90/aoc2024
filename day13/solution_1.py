import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Button:
    x: int
    y: int


@dataclass
class Prize:
    x: int
    y: int


@dataclass
class Machine:
    button_a: Button 
    button_b: Button
    prize: Prize

    @staticmethod
    def from_str(machine_def: str):
        raw = machine_def.strip().split('\n')
        buttons = [int(entry) for entry in re.findall(r'[X|Y]\+(\d+)', machine_def)]
        prize = [int(entry) for entry in re.findall(r'[X|Y]\=(\d+)', machine_def)]
        button_a = Button(x=buttons[0], y=buttons[1])
        button_b = Button(x=buttons[2], y=buttons[3])
        prize = Prize(x=prize[0], y=prize[1])
        return Machine(button_a, button_b, prize)


TOKEN_COST = {
    "A": 3,
    "B": 1,
}


def parse_input(puzzle_input: str) -> list[Machine]:
    return [Machine.from_str(m) for m in puzzle_input.strip().split('\n\n')]


def calculate_button_presses(machine: Machine) -> Optional[dict]:
    """Find the right amount of button presses or return `None` if impossible."""
    # First try to calculate the minimum number of times either button
    # has to be pressed to reach the prize location
    # We could calculate this for either 'x' or 'y' values, but in this
    # case we calculate the "ratio" for the x value.
    multiplier_a = machine.prize.x // machine.button_a.x
    multiplier_b = machine.prize.x // machine.button_b.x

    for multiplier in (multiplier_a, multiplier_b):
        for i in range(multiplier):
            for j in range(multiplier, 0, -1):  # Reverse range
                # For increasing i; the value of j is decreasing
                total_x = machine.button_a.x * i + machine.button_b.x * j
                total_y = machine.button_a.y * i + machine.button_b.y * j

                if total_x == machine.prize.x and total_y == machine.prize.y:
                    return {
                        "A": i,
                        "B": j,
                    }

    # If no solution is possible, return None
    return None


def main():
    with open('day13/input_1.txt') as f:
        puzzle_input = f.read()

    machines = parse_input(puzzle_input)

    total_token_cost = 0
    for m in machines:
        presses = calculate_button_presses(m)
        if presses is not None:
            total_token_cost += TOKEN_COST["A"] * presses["A"]
            total_token_cost += TOKEN_COST["B"] * presses["B"]

    print(f'Minimum amount of tokens spend to obtain all prizes: {total_token_cost}.')


if __name__ == "__main__":
    main()
