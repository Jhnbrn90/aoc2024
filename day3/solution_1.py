import re

def parse_input(puzzle_input: str) -> list[str]:
    """Extract the multiplication instructions from raw input."""
    regex = r'mul\(\d{1,3},\s{0,1}\d{1,3}\)'
    matches = re.findall(regex, puzzle_input)
    return matches


def execute_mul_instruction(instruction: str) -> int:
    """"Parse `mul` instruction and yield the sum of provided values."""
    regex = r'mul\((\d+),\s{0,1}(\d+)\)'
    matches = re.match(regex, instruction)
    product = int(matches.group(1)) * int(matches.group(2))
    return product

def main():
    with open('day3/input_1.txt') as f:
        puzzle_input = f.read()

    instructions = parse_input(puzzle_input)

    list_of_products = [execute_mul_instruction(instruction) for instruction in instructions]

    print(f"Sum: {sum(list_of_products)}")


if __name__ == "__main__":
    main()