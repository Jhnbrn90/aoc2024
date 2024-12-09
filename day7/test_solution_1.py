from collections import OrderedDict
from solution_1 import parse_input


with open('day7/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()


def test_parse_input():
    expected = OrderedDict({
        190: [10, 19],
        3267: [81, 40, 27],
        83: [17, 5],
        156: [15, 6],
        7290: [6, 8, 6, 15],
        161011: [16, 10, 13],
        192: [17, 8, 14],
        21037: [9, 7, 18, 13],
        292: [11, 6, 16, 20],
    })
    result = parse_input(SAMPLE_INPUT)
    assert result == expected
