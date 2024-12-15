from solution_1 import parse_input_to_grid, traverse_grid_optimized, LoopException


def is_loop(grid: list[list[str]]) -> bool:
    """Check if the current grid results in a loop."""
    try:
        traverse_grid_optimized(grid)
    except LoopException:
        return True
    return False


def main():
    with open(f'day06/input_1.txt') as f:
        puzzle_input = f.read()

    grid = parse_input_to_grid(puzzle_input)
    visits = traverse_grid_optimized(grid)
    loop_positions = set()

    loop_count = 0
    for row, column, direction in visits:
        if grid[row][column] == ".":
            # Place obstacle and check if guard ends up in loop
            grid[row][column] = "#"
            if is_loop(grid):
                loop_positions.add((row, column))
            # Remove obstacle for next iteration
            grid[row][column] = "."

    loop_count = len(loop_positions)
    print(f"Possible (unique) object placements: {loop_count}.")

if __name__ == "__main__":
    main()
