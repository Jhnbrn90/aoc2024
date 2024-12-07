import pytest
from collections import defaultdict

from solution_1 import validate_update
from solution_2 import correctly_order_update_line


RULES_DICT = defaultdict(set)
RULES_DICT['1'].add('2')
RULES_DICT['2'].add('3')

@pytest.mark.parametrize('update,correct_order', [
    (['1', '3', '2'], ['1', '2', '3']),
])
def test_correctly_order_update_line(update, correct_order):
    assert validate_update(['1', '2', '3'], RULES_DICT) == True
    assert correctly_order_update_line(update, RULES_DICT) == correct_order
