from collections import defaultdict


MATCH_WORD = "XMAS"


def parse_input_to_grid(puzzle_input: str) -> list[list[str]]:
    grid = [list(line) for line in puzzle_input.strip().split('\n')]
    return grid


def find_matches_in_line(line: list[str]) -> int:
    """Analyze given line and return the count of matches."""
    line_str = "".join(line)

    normal = MATCH_WORD
    backwards = "".join(reversed(MATCH_WORD))

    return line_str.count(normal) + line_str.count(backwards)


def horizontal_matches(grid: list[list[str]]) -> int:
    return sum([find_matches_in_line(line) for line in grid])


def vertical_matches(grid: list[list[str]]) -> int:
    row_count = len(grid)
    column_count = len(grid[0])
    vertical_lines = defaultdict(list)

    for column in range(column_count):
        for row in range(row_count):
            vertical_lines[column].append(grid[row][column])

    lines = vertical_lines.values()

    return sum([find_matches_in_line(line) for line in lines])


def diagonal_matches(grid: list[list[str]]) -> int:
    """
        0 1 2 3 4 5
    0   x y z
    1     x y z
    2       x y z
    3         x y z
    4           x y
    5             x y

    Diagonal matches are recognised by the constant difference between row/column.
    For diagonal `x`, this difference is 0, for `y` it is 1, for `z` it is 2, etc.
    Therefore, we can iterate through the grid and store each value under a key `r-c`
    (or `c-r`).

    The anti-diagonal runs from top-right to bottom-left.

        0 1 2 3 4 5
    0             x      
    1           x 
    2         x 
    3       x 
    4     x 
    5   x 
    
    The values on this diagonal share the sum of the coordinates (`r+c`).
    """
    row_count = len(grid)
    column_count = len(grid[0])

    # Two default dicts, to prevent overlap of the key values for the
    # "regular" diagonal and the "anti" diagonal.
    diagonals = defaultdict(list)
    anti_diagonals = defaultdict(list)

    for row in range(row_count):
        for column in range(column_count):
            diagonals[row-column].append(grid[row][column])
            anti_diagonals[row+column].append(grid[row][column])

    lines = list(diagonals.values()) + list(anti_diagonals.values())
    return sum([find_matches_in_line(line) for line in lines])


def main():
    with open('day4/input_1.txt') as f:
        puzzle_input = f.read()

    grid = parse_input_to_grid(puzzle_input)

    horizontal = horizontal_matches(grid)
    vertical = vertical_matches(grid)
    diagonal = diagonal_matches(grid)

    total = horizontal + vertical + diagonal

    print(f"Total: {total}.")

if __name__ == "__main__":
    main()
