import pytest

from solution import get_similarity_scores


@pytest.mark.parametrize('lists_input,expected', [
    ([[1, 2, 3], [3, 4, 5]], [0, 0, 3]),
    ([[4, 5, 3], [3, 3, 3, 9, 16]], [0, 0, 9]),

])
def test_find_similarity(lists_input, expected):
    assert get_similarity_scores(lists_input) == expected
