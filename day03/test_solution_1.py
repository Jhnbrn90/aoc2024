import pytest

from solution_1 import (
    execute_mul_instruction,
    parse_input
)

with open('day03/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()


def test_it_parses_the_multiplications():
    """Check that the puzzle input is parsed into `mul()` instructions."""
    assert parse_input(SAMPLE_INPUT) == [
        "mul(2,4)",
        "mul(5,5)",
        "mul(11,8)",
        "mul(8,5)",
    ]


@pytest.mark.parametrize('instruction,expected', [
    ('mul(2,4)', 8),
    ('mul(218,42)', 9156),
    ('mul(10,4)', 40),
    ('mul(28, 312)', 8736),
])
def test_execute_multiplication_instruction(instruction: str, expected: int):
    """Check that the `mul()` instructions can be used to yield the corresponding products."""
    result = execute_mul_instruction(instruction)
    assert result == expected
