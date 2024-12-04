import pytest


from solution import (
    calculate_distance,
    string_to_list
)


with open('day1/1/sample.txt') as f:
    SAMPLE_INPUT = f.read()


def test_string_to_lists():
    result = string_to_list(SAMPLE_INPUT)

    expected = [
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3],
    ]

    assert result == expected


@pytest.mark.parametrize('list_input,expected', [
    ([[9, 8, 7], [9, 8, 7]], [0, 0, 0]),  # equal values
    ([[4, 2, 1], [1, 2, 3]], [3, 0, 2]),  # left greater
    ([[1, 2, 3], [4, 2, 1]], [3, 0, 2]),  # right greater
])
def test_something(list_input, expected):
    assert calculate_distance(list_input) == expected
