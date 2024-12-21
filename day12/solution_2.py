from solution_1 import DIRECTIONS, garden_plot, parse_to_grid, get_perimeters


def get_sides(garden_plot: set[tuple]) -> int:
    """Get the number of sides for a given garden plot."""
    perimeters = get_perimeters(garden_plot)

    sides = 0
    while perimeters:
        # Each perimeter consists of a (x,y) coordinate and
        # a direction vector (i.e. the direction we were exploring
        # when this perimeter was found).
        x, y, direction = perimeters.pop()
        sides += 1

        # Either dx or dy is 0 in this stage
        # If the perimeter was placed along the 'x' axis (dx != 0)
        # we want to explore the y-axis and vice versa.

        # # if perimeter.dx == 0:
        # if pdy == 0:
        #     # The perimeter is oriented vertically
        #     # Find perimeters along the y-axis
        #     explore_direction_xy = ((0, -1), (0, 1))
        # elif pdx == 0:
        # # elif perimeter.dy == 0:
        #     # The perimeter is oriented horizontally
        #     # Find perimeters along the x-axis
        #     explore_direction_xy = ((-1, 0), (1, 0))

        # Explore the perimeter in both x and y direction.
        explore_direction_xy = (
            # Along x-axis
            (-1, 0), (1, 0),
            # Along the y-axis
            (0, -1), (0, 1),
        )

        # for dx, dy in explore_direction_xy:
        for dx, dy in explore_direction_xy:
            next_x = x + dx
            next_y = y + dy

            while True:
                try:
                    perimeters.remove((next_x, next_y, direction))
                    next_x += dx
                    next_y += dy
                except ValueError:
                    # Stop when there are no more neighbouring perimeters
                    # to remove from the perimeters for the given direction
                    break

    return sides


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
            sides = get_sides(plot)

            total_sum += area*sides

    print(total_sum)


if __name__ == "__main__":
    main()
