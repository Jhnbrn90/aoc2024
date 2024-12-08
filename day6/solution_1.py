# Directions mapping of direction to "move" action
# which represents the (row, column) coordinate update
# that corresponds with the given applied direction.
DIRECTION_MOVE = {
    # up
    "up": (-1, 0),  # column constant, row moves up
    "right": (0, +1),  # row constant, column moves right
    "down": (+1, 0),  # column costant, row moves down
    "left": (0, -1),  # row constant, column moves left
}


# Mapping of character to direction within the grid
CHARACTER_DIRECTION = {
    "^": "up",
    ">": "right",
    "v": "down",
    "<": "left",
}


DIRECTIONS_ORDER = ["up", "right", "down", "left"]


class PathException(Exception):
    pass


def get_next_direction(current_direction: str) -> str:
    """Get the next direction given current_direction."""
    current_idx = DIRECTIONS_ORDER.index(current_direction)

    try:
        return DIRECTIONS_ORDER[current_idx + 1]
    except IndexError:
        return DIRECTIONS_ORDER[0]


def parse_input_to_grid(puzzle_input: str) -> list[list[str]]:
    return [list(line) for line in puzzle_input.strip().split('\n')]


def find_initial_coordinate_and_direction(grid: list[list[str]]) -> str:
    row_count = len(grid)
    column_count = len(grid[0])

    for row in range(row_count):
        for column in range(column_count):
            coordinate = (row, column)
            value = grid[row][column]
            if value in CHARACTER_DIRECTION.keys():
                return coordinate, CHARACTER_DIRECTION[value]
    else:
        raise ValueError("No starting coordinate found.")


def get_next_coordinates(grid: list[list[str]]) -> tuple:
    """Based on the current grid, get next coordinates.
    current: (1, 1)
    action: (-1, 0)
    -------------- + 
    new:   (0, 1)
    """
    coordinates, direction = find_initial_coordinate_and_direction(grid)
    next_action = DIRECTION_MOVE[direction]
    return tuple(map(sum, zip(coordinates, next_action)))


def perform_move(grid: list[list[str]]) -> list[list[str]]:
    """Update grid by taking 1 step."""
    # Peek at the next spot in the grid
    row_count = len(grid)
    column_count = len(grid[0])

    row, column = get_next_coordinates(grid)

    if row > row_count - 1 or column > column_count - 1:
        raise IndexError("reached the end of the grid.")
    if row < 0 or column < 0:
        raise IndexError("reached the end of the grid.")

    if grid[row][column] == '#':
        raise PathException("reached end of path")

    # mark current position with "X"
    # move to new position
    coordinates, direction = find_initial_coordinate_and_direction(grid)
    initial_row, initial_column = coordinates

    DIRECTION_CHARACTER = {v: k for k, v in CHARACTER_DIRECTION.items()}
    grid[initial_row][initial_column] = 'X'
    grid[row][column] = DIRECTION_CHARACTER[direction]

    return grid


def traverse_grid(grid: list[list[str]]) -> list[list[str]]:
    """Traverse the grid and return the result."""
    DIRECTION_CHARACTER = {v: k for k, v in CHARACTER_DIRECTION.items()}

    while True:
        coordinates, direction = find_initial_coordinate_and_direction(grid)
        row, column = coordinates
        try:
            grid = perform_move(grid)
        except PathException:
            next_direction = get_next_direction(direction)
            # Change current direction
            grid[row][column] = DIRECTION_CHARACTER[next_direction]
        except IndexError:
            # At the end of the grid
            # Highlight current position as marked
            grid[row][column] = 'X'
            break

    return grid


def count_visits(grid: list[list[str]]) -> int:
    total_visisted = 0 
    for row in grid:
        for column in row:
            total_visisted += column.count('X')

    return total_visisted


def main():
    with open(f'day6/input_1.txt') as f:
        puzzle_input = f.read()

    grid = parse_input_to_grid(puzzle_input)
    path = traverse_grid(grid)

    print(f"Took path: {path}")
    visits = count_visits(path)
    print(f"Counted {visits} visits.")


if __name__ == "__main__":
    main()
