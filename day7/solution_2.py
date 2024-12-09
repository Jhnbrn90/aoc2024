import re
import itertools
from collections import OrderedDict

def parse_input(puzzle_input: str) -> dict:
    input_dict = OrderedDict()

    entries = puzzle_input.strip().split('\n')
    for entry in entries:
        test_sum, calibration_values = entry.split(':')
        calibration_values = [int(value) for value in calibration_values.strip().split(' ')]
        input_dict[int(test_sum)] = calibration_values

    return input_dict


def main():
    with open(f'day7/input_1.txt') as f:
        puzzle_input = f.read()
    
    input_dict = parse_input(puzzle_input)

    valid_operations = []
    for test_sum, calibration_values in input_dict.items():
        # Get all permutations for + / * for the given length of
        # the calibration values
        
        number_of_operations = len(calibration_values) - 1
        # calculate the number of possible permutations for a given list of integers
        # for the possibilities: + or *.
        symbols = ['||', '*', '+']
        operation_permutations = itertools.product(symbols, repeat=number_of_operations)

        for permutation in operation_permutations:
            # print(f"Performing permutation: {permutation} on {calibration_values}")
            # Each permutations consist of a tuple of + or * operations
            result = calibration_values[0]
            for i, symbol in enumerate(permutation):
                if symbol == "+":
                    result = result + calibration_values[i+1]
                if symbol == "*":
                    result = result * calibration_values[i+1]
                if symbol == "||":
                    result = int(f"{result}{calibration_values[i+1]}")

            if result == test_sum:
                valid_operations.append(test_sum)
                break  # stop if we found that the permutation was valid

    # print(valid_operations)
    print(f"Sum of valid operations: {sum(valid_operations)}")

if __name__ == "__main__":
    main()
