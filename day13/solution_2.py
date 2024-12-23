"""
In part 2, we have to be more clever as the target coordinates get
increased to such an extent that the simple approach takes way too long.

The equations we need to solve, if we assume "i" presses of button A and "j"
presses of button B are as follows (P is prize):
    - i * A.y + j * B.y == P.y
    - i * A.x + j * B.x == P.x

We can only solve i in terms of j, and vice versa.
For example:
    - i = (P.x - j*B.x) / A.x
    - j = (p.y - i*A.y) / B.y

To solve one of those into only known terms, Cramer's rule can be used.
https://en.wikipedia.org/wiki/Cramer%27s_rule

This rule states that these simple systems can be written as follows.
Given our equations listed above, these rules dictate the following
solutions for i and j in only known terms:
    - i = (P.x*B.y - B.x*P.y) / (A.x*B.y - A.y*B.x)
    - j = (P.y*A.x - P.x*A.y) / (A.x*B.y - A.y*B.x)

We only need one of these, as we already have i in terms of j and vice versa.
"""
from typing import Optional

from solution_1 import (
    Machine,
    parse_input,
    TOKEN_COST,
)


def calculate_cramer_solution(machine: Machine) -> Optional[dict]:
    a = machine.button_a
    b = machine.button_b
    p = machine.prize

    # Use the Cramer's Rule method to obtain `i`
    i = (p.x * b.y - b.x * p.y) / (a.x * b.y - a.y * b.x)
    # Now we have `i`, we can calculate `j` through substitution
    j = (p.y - i * a.y) / b.y

    # Or use the Cramer's Rule to obtain an expression of `j`
    ## j = (p.y * a.x - p.x * a.y) / (a.x * b.y - a.y * b.x)

    if i.is_integer() and i >= 0 and j.is_integer() and j >= 0:
        return {
            "A": int(i),
            "B": int(j),
        }

    return None


def main():
    with open('day13/input_1.txt') as f:
        puzzle_input = f.read()

    machines = parse_input(puzzle_input)

    total_token_cost = 0
    for machine in machines:
        machine.prize.x += 10000000000000
        machine.prize.y += 10000000000000

        result = calculate_cramer_solution(machine)

        if result is not None:
            total_token_cost += result["A"] * TOKEN_COST["A"]
            total_token_cost += result["B"] * TOKEN_COST["B"]

    print(f"Token cost: {total_token_cost}")


if __name__ == "__main__":
    main()
