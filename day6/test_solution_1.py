import pytest


from solution_1 import (
    parse_input_to_grid,
    get_next_direction,
    find_initial_coordinate_and_direction,
    get_next_coordinates,
    perform_move,
    PathException,
    traverse_grid,
    count_visits,
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


@pytest.mark.parametrize('initial,moved', [
    ([
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '^', '.'],
    ], [
        ['.', '.', '.'],
        ['.', '^', '.'],
        ['.', 'X', '.'],
    ]),
    ([
        ['.', '.', '.'],
        ['>', '.', '.'],
        ['X', 'X', '.'],
    ], [
        ['.', '.', '.'],
        ['X', '>', '.'],
        ['X', 'X', '.'],
    ]),
])
def test_perform_move_valid(initial, moved):
    assert perform_move(initial) == moved


@pytest.mark.parametrize('grid', [
    [
        ['.', '.', '>'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ],
    [
        ['.', '.', '^'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ],
    [
        ['<', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ],
    [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', 'v', '.'],
    ],
])
def test_perform_move_end_of_grid(grid):
    with pytest.raises(IndexError):
        perform_move(grid)


@pytest.mark.parametrize('grid', [
    [
        ['.', '#', '<'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ],
    [
        ['.', '#', '.'],
        ['.', '^', '.'],
        ['.', '.', '.'],
    ],
    [
        ['>', '#', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ],
    [
        ['.', 'v', '.'],
        ['.', '#', '.'],
        ['.', '.', '.'],
    ],
])
def test_perform_move_hit_road_block(grid):
    with pytest.raises(PathException):
        perform_move(grid)


@pytest.mark.parametrize('grid,expected', [
    ([
        ['.', '#', '.'],
        ['.', '.', '.'],
        ['.', '^', '.'],
    ], [
        ['.', '#', '.'],
        ['.', 'X', 'X'],
        ['.', 'X', '.'],
    ]),
    ([
        ['#', '.', '.'],
        ['.', '.', '#'],
        ['^', '.', '.'],
    ], [
        ['#', '.', '.'],
        ['X', 'X', '#'],
        ['X', 'X', '.'],
    ]),
])
def test_traverse_grid(grid, expected):
    assert traverse_grid(grid) == expected


def test_traverse_grid_sample():
    with open('day6/sample_output_1.txt') as f:
        sample_output = f.read()

    sample_input_grid = parse_input_to_grid(SAMPLE_INPUT)
    expected_output = parse_input_to_grid(sample_output)
    assert traverse_grid(sample_input_grid) == expected_output

@pytest.mark.parametrize('grid,count', [
    ([
        ['X', '#', '.'],
        ['X', '.', '.'],
        ['X', 'X', '.'],
    ], 4),
    ([
        ['X', '#', '.'],
        ['X', 'X', '.'],
        ['X', 'X', '.'],
    ], 5),
    ([
        ['.', '#', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ], 0),
])
def test_count_visits(grid, count):
    assert count_visits(grid) == count
