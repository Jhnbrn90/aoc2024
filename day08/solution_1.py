from collections import defaultdict


def parse_input(puzzle_input: str) -> list[list[str]]:
    """Parse puzzle input into a grid."""
    grid = [list(row) for row in puzzle_input.strip().split('\n')]
    return grid


def get_node_coordinates(grid: list[list[str]]) -> dict[str, list[tuple]]:
    """Get list of coordinate tuples for nodes."""
    height = len(grid)
    width = len(grid[0])
    nodes = defaultdict(list)

    for y in range(height):
        for x in range(width):
            character = grid[y][x]
            if character != '.':
                # Found a node
                nodes[character].append((y, x))
    return nodes


def get_anti_node_coordinates(grid: list[list[str]], nodes: dict[str,list[tuple]]) -> set[tuple]:
    antinode_coordinates = set()

    height = len(grid)
    width = len(grid[0])

    for antenna, coordinates in nodes.items():
        coordinate_count = len(coordinates)
        for i in range(coordinate_count):
            for j in range(i+1, coordinate_count):
                # Get a pair of coordinates
                y1, x1 = coordinates[i]
                y2, x2 = coordinates[j]

                # Calculate the distances
                dy = y2 - y1
                dx = x2 - x1

                # Positions of antinode
                antinodes = [
                    {"x": x1-dx, "y": y1-dy},  # to the "left" of node
                    {"x": x2+dx, "y": y2+dy},  # to the "right" of node
                ]

                for antinode in antinodes:
                    # Check if antinode is within the grid
                    if 0 <= antinode['x'] < width and 0 <= antinode['y'] < height:
                        antinode_coordinates.add((antinode['y'], antinode['x']))

    return antinode_coordinates


def main():
    with open('day08/input_1.txt') as f:
        puzzle_input = f.read()

    grid = parse_input(puzzle_input)
    nodes = get_node_coordinates(grid)
    anti_nodes = get_anti_node_coordinates(grid, nodes)

    print(f"Possible antinodes: {len(anti_nodes)}.")


if __name__ == "__main__":
    main()
