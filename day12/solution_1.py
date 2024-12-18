# Coordinates of neighbouring plants
DIRECTIONS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)


def parse_to_grid(puzzle_input: str) -> list[list[str]]:
    return [list(row) for row in puzzle_input.strip().split('\n')]


def garden_plot(grid, x, y, visited):
    """Get the coordinates of a garden plot for a specific plant type."""
    if (x,y) not in visited:
        visited.add((x, y))

        for dx, dy in DIRECTIONS:
            nx = x+dx
            ny = y+dy

            if not (0 <= ny < len(grid) and 0 <= nx < len(grid[0])):
                # If the coordinates are out of bound, skip
                continue

            if grid[ny][nx] == grid[y][x]:
                # If the neighbour plant belongs to the same type,
                # it should be added to the visited set and also
                # be traversed in each direction.
                garden_plot(grid, nx, ny, visited)

    return visited


def get_perimeter(garden_plot: set[tuple]):
    """Get the perimeter for a given garden plot."""
    perimeter = 0
    for (x, y) in garden_plot:
        # An isolated plant has a perimeter of 4
        perimeter += 4
        for (dx, dy) in DIRECTIONS:
            if (x+dx, y+dy) in garden_plot:
                perimeter -= 1

    return perimeter


def main():
    with open('day12/input_1.txt') as f:
        puzzle_input = f.read()

    grid = parse_to_grid(puzzle_input)
    height = len(grid)
    width = len(grid[0])

    covered_plots = set()

    total_sum = 0

    for y in range(height):
        for x in range(width):
            if (x, y) in covered_plots:
                continue
            
            plot = garden_plot(grid, x, y, set())
            covered_plots.update(plot)

            area = len(plot)
            perimeter = get_perimeter(plot)

            total_sum += area*perimeter

    print(total_sum)


if __name__ == "__main__":
    main()
