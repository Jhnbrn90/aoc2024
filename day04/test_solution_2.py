from solution_1 import parse_input_to_grid
from solution_2 import find_cross_mas_diagonally


with open('day04/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()


def test_it_finds_xmas_shapes():
    grid = parse_input_to_grid(SAMPLE_INPUT)
    result = find_cross_mas_diagonally(grid)

    assert result == 9
