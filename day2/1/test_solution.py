import pytest


from solution import (
    get_levels_from_input,
    level_is_safe
)


with open('day2/1/sample.txt') as f:
    SAMPLE_INPUT = f.read()


def test_get_levels_from_input():
    levels = get_levels_from_input(SAMPLE_INPUT)
    assert levels == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


@pytest.mark.parametrize('level,is_safe', [
    ([1, 2, 3], True),  # ascending
    ([3, 2, 1], True),  # descending
    ([10, 7, 6], True),  # maximum difference is three
    ([1, 4, 5], True),  # maximum difference is three
    ([10, 6, 5], False),  # maximum difference exceeded
    ([1, 5, 6], False),  # maximum difference exceeded
    ([1, 1, 2], False),  # minimum difference is one
    ([2, 2, 1], False),  # minimum difference is one
    ([1, 2, 1], False),  # both ascending and descending
    ([1, 3, 2, 4, 5], False),  # both ascending and descending
])
def test_level_is_safe(level, is_safe):
    assert level_is_safe(level) == is_safe
