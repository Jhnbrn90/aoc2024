from solution_1 import parse_input_to_grid


def find_cross_mas_diagonally(grid: list[list[str]]):
    """Find cross-text 'MAS' with 'A' as center.

    Given that we have the following grid:

        0   1   2   3
    0   M       M
    1       A
    2   S       S
    3

    The grid above contains crossed (X) "MAS" diagonally.

    Given that the center coordinate is (1,1) (i.e. (row, column)):

    center: (1,1)
    top-left: (0, 0); relative to center: (-1, -1)
    top-right: (0, 2); relative to center: (-1, +1)
    bottom-left: (2, 0); relative to center: (+1, -1)
    bottom-right: (2, 2); relative to center: (+1, +1)

    The coordinates surrounding "A" with "M" and "S" are paired
    as follows:
     - diagonal 1: top-left + bottom-right
     - diagonal 2: bottom-left + top-right

    These pairs should contain the set of "M" and "S" to form "MAS".
    It does not matter which letter, as it can be read backwards.
    """
    row_count = len(grid)
    column_count = len(grid[0])
    matches = 0

    # Since there can't be any centered "A" on the first/last row
    # or on the first/last column, these are excluded from the range
    for row in range(1, row_count-1):
        for column in range(1, column_count-1):
            # Check if current letter is "A"
            if grid[row][column] == "A":
                # Check the surrounding diagonal letters
                top_left = grid[row-1][column-1]
                top_right = grid[row-1][column+1]
                bottom_left = grid[row+1][column-1]
                bottom_right = grid[row+1][column+1]

                # Diagonal 1 (top-left + bottom-right)
                if not set({top_left, bottom_right}) == set({"M", "S"}):
                    continue

                # Diagonal 2 (bottom-left + top-right)
                if not set({bottom_left, top_right}) == set({"M", "S"}):
                    continue

                # Both diagonals are validated and spell "MAS"
                matches += 1

    return matches


def main():
    with open('day04/input_1.txt') as f:
        puzzle_input = f.read()

    grid = parse_input_to_grid(puzzle_input)
    mas_matches = find_cross_mas_diagonally(grid)

    print(f"Found {mas_matches} matches.")


if __name__ == "__main__":
    main()
