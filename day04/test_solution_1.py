from solution_1 import (
    parse_input_to_grid,
    horizontal_matches,
    vertical_matches,
    diagonal_matches,
)


with open('day04/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()


def test_parse_input_to_grid():
    result = parse_input_to_grid(SAMPLE_INPUT)
    
    assert result == [
        ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
        ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
        ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
        ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
        ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
        ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
        ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
        ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
        ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
        ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X'],
    ]


def test_traverse_horizontally_both():
    grid = parse_input_to_grid(SAMPLE_INPUT)
    result = horizontal_matches(grid)
    assert result == 5


def test_traverse_vertically():
    """Check that vertically spelled words are found."""
    grid = parse_input_to_grid(SAMPLE_INPUT)
    result = vertical_matches(grid)
    assert result == 3


def test_traverse_diagonally():
    grid = parse_input_to_grid(SAMPLE_INPUT)
    result = diagonal_matches(grid)
    assert result == 10


def test_traverse_complete_grid():
    grid = parse_input_to_grid(SAMPLE_INPUT)
    horizontal = horizontal_matches(grid)
    vertical = vertical_matches(grid)
    diagonal = diagonal_matches(grid)

    total = horizontal + vertical + diagonal
    assert total == 18
 

