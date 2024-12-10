from solution_1 import (
    parse_input,
    get_node_coordinates,
)


def find_antinodes(grid, nodes):
    height = len(grid)
    width = len(grid[0])

    antinode_coordinates = set()
    for node, coordinates in nodes.items():
        coordinate_count = len(coordinates)
        for i in range(coordinate_count):
            for j in range(i + 1, coordinate_count):
                y1, x1 = coordinates[i]
                y2, x2 = coordinates[j]

                # Difference
                dy = y2 - y1
                dx = x2 - x1

                # Nodes
                left_node = {"x": x1, "y": y1}
                right_node = {"x": x2, "y": y2}

                # Walk left until reaching the boundaries of the grid
                y = left_node['y']
                x = left_node['x']
                while (0 <= x < width and 0 <= y < height):
                    antinode_coordinates.add((y, x))
                    x -= dx
                    y -= dy

                # Might be extracted to dedicated walk function in a later stage

                # Walk right until reaching the boundaries of the grid
                y = right_node['y']
                x = right_node['x']
                while (0 <= x < width and 0 <= y < height):
                    antinode_coordinates.add((y, x))
                    x += dx
                    y += dy

    return antinode_coordinates


def main():
    with open('day8/input_1.txt') as f:
        puzzle_input = f.read()

    grid = parse_input(puzzle_input)
    nodes = get_node_coordinates(grid)
    antinodes = find_antinodes(grid, nodes)

    print(f"Number of antinodes: {len(antinodes)}.")


if __name__ == "__main__":
    main()
