""""
New conditionals to consider:
 - do(): enables future mul() instructions
 - don't(): disables future mul() instructions

 Only most recent do() or don't() applies.
 At the beginning all mul() instructions are enabled.
"""

import re

from solution_1 import (
    parse_input,
    execute_mul_instruction,
)

def extract_valid_multiplication_instructions(puzzle_input: str) -> str:
    # Find all instructions
    valid_instructions = ""
    regex = r"mul\((\d{1,3}),\s{0,1}(\d{1,3})\)|do\(\)|don't\(\)"
    instructions_enabled = True

    for match in re.finditer(regex, puzzle_input):
        found_inst = match.group(0)
        if 'mul(' in found_inst:
            # Found a multiplication instruction
            if instructions_enabled:
                # only add it to the list of valid instructions
                # if currently in "enabled" mode
                valid_instructions += found_inst
        elif found_inst.startswith("don't("):
            # When matching a "don't" instruction, set
            # the current mode accordingly.
            instructions_enabled = False
        elif found_inst.startswith("do("):
            # When matching a "do" instruction, the
            # mode should be in enabled state.
            instructions_enabled = True
        else:
            print(f"Unexpected match: {found_inst}.")

    return valid_instructions


def main():
    with open('day03/input_1.txt') as f:
        # We're using the same input as part 1
        puzzle_input = f.read()

    valid_mult_instructions = extract_valid_multiplication_instructions(puzzle_input)
    instructions = parse_input(valid_mult_instructions)
    list_of_products = [execute_mul_instruction(instruction) for instruction in instructions]

    print(f"Sum: {sum(list_of_products)}.")

if __name__ == "__main__":
    main()
