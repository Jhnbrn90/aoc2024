import pytest

from solution_1 import blink, count_stones, normalise_zeros, perform_blinks

@pytest.mark.parametrize('input_str,expected', [
    ('000', '0'),
    ('000000', '0'),
    ('000001', '1'),
    ('001234', '1234'),
    ('0012340', '12340'),
    ('00123400', '123400'),
])
def test_normalise_zeros(input_str: str, expected: str):
    assert normalise_zeros(input_str) == expected


@pytest.mark.parametrize('initial,expected', [
    ('0 1 10 99 999', '1 2024 1 0 9 9 2021976'),
    # after 1 blink
    ('125 17', '253000 1 7'),
    # after 2 blinks
    ('253000 1 7', '253 0 2024 14168'),
    # after 3 blinks
    ('253 0 2024 14168', '512072 1 20 24 28676032'),
    # after 4 blinks
    ('512072 1 20 24 28676032', '512 72 2024 2 0 2 4 2867 6032'),
    # After 5 blinks
    ('512 72 2024 2 0 2 4 2867 6032', '1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32'),
    # After 6 blinks
    ('1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32', '2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2'),
])
def test_blink_once(initial:str, expected: str):
    assert blink(initial) == expected


def test_count_stones():
    assert count_stones('2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2') == 22


def test_blink_number_of_times():
    initial_arrangement = '125 17'
    blink_count = 25
    final_stone_count = 55312

    stones = perform_blinks(initial_arrangement, blink_count)

    assert count_stones(stones) == final_stone_count