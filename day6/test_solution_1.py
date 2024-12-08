import pytest


from solution_1 import (
    parse_input_to_grid,
    get_next_direction,
    find_initial_coordinate_and_direction,
    get_next_coordinates,
)


with open('day6/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()


def test_parse_input_to_grid():
    assert parse_input_to_grid(SAMPLE_INPUT) == [
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ]


@pytest.mark.parametrize('current_direction,expected_next', [
    ('up', 'right'),
    ('right', 'down'),
    ('down', 'left'),
    ('left', 'up'),
])
def test_get_next_direction(current_direction, expected_next):
    assert get_next_direction(current_direction) == expected_next


@pytest.mark.parametrize('grid,expected_coordinates,expected_direction', [
    ([
        ['.', '.', '.'],
        ['.', '>', '.'],
        ['.', '.', '.'],
    ], (1, 1), "right"),
    ([
        ['.', '.', 'v'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ], (0, 2), "down"),
    ([
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['<', '.', '.'],
    ], (2, 0), "left"),
    ([
        ['.', '^', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ], (0, 1), "up"),
])
def test_get_initial_direction(grid, expected_coordinates, expected_direction):
     coordinate, direction = find_initial_coordinate_and_direction(grid)
     assert coordinate == expected_coordinates
     assert direction == expected_direction


def test_get_initial_direction_invalid():
    grid_without_start = [
        ['.', '#', '.'],
        ['.', '.', '.'],
        ['#', '.', '.'],
    ]

    with pytest.raises(ValueError):
        find_initial_coordinate_and_direction(grid_without_start)


def test_get_initial_direction_sample_input():
     grid = parse_input_to_grid(SAMPLE_INPUT)
     coordinate, direction = find_initial_coordinate_and_direction(grid)
     assert coordinate == (6, 4)
     assert direction == "up"



@pytest.mark.parametrize('grid,next_coordinates', [
    ([
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '^', '.'],
    ], (1, 1)),
    ([
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '<', '.'],
    ], (2, 0)),
    ([
        ['v', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ], (1, 0)),
    ([
        ['>', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ], (0, 1)),
])
def test_get_next_coordinates(grid, next_coordinates):
    assert get_next_coordinates(grid) == next_coordinates
