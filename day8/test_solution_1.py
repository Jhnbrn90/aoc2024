from solution_1 import parse_input, get_node_coordinates, get_anti_node_coordinates


with open('day8/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()


def test_parse_input():
    grid = parse_input(SAMPLE_INPUT)

    assert grid == [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]


def test_get_coordinates_of_nodes():
    grid = parse_input(SAMPLE_INPUT)
    result = get_node_coordinates(grid)
    assert result == {
        '0': [(1, 8), (2, 5), (3, 7), (4, 4)],
        'A': [(5, 6), (8, 8), (9, 9)],
    }


def test_get_coordinates_of_anti_nodes():
    grid = parse_input(SAMPLE_INPUT)
    nodes = get_node_coordinates(grid)
    antinodes = get_anti_node_coordinates(grid, nodes)
    assert antinodes  == {
        (2, 4), (11, 10), (7, 7), (4, 9), (2, 10), (7, 0), (5, 1), (0, 6), (10, 10), (5, 6), (3, 2), (6, 3), (1, 3), (0, 11)
    }
    assert len(antinodes) == 14
