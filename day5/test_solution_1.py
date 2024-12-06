import pytest

from solution_1 import parse_input, rules_to_dictionary, validate_update


with open('day5/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()


def test_parse_input():
    """Check the parsed input provides rules and updates."""
    rules, updates = parse_input(SAMPLE_INPUT)

    assert rules == [
        '47|53',
        '97|13',
        '97|61',
        '97|47',
        '75|29',
        '61|13',
        '75|53',
        '29|13',
        '97|29',
        '53|29',
        '61|53',
        '97|53',
        '61|29',
        '47|13',
        '75|47',
        '97|75',
        '47|61',
        '75|61',
        '47|29',
        '75|13',
        '53|13',
    ]
    assert updates == [
        ['75', '47', '61', '53', '29'],
        ['97', '61', '53', '29', '13'],
        ['75', '29', '13'],
        ['75', '97', '47', '61', '53'],
        ['61', '13', '29'],
        ['97', '13', '75', '29', '47'],
    ]


@pytest.mark.parametrize('rules,expected', [
    (['1|2', '3|4'], {"1": {"2"}, "3": {"4"}}),
    (['71|3', '12|34', '5|55', '71|5'], {"71": {"3", "5"}, "12": {"34"}, "5": {"55"}}),
])
def test_rule_dictionary(rules, expected):
    """Check that rules are parsed into dictionary."""
    assert rules_to_dictionary(rules) == expected


@pytest.mark.parametrize('update,rules,is_valid', [
    (['1', '2', '3'], ['1|2', '2|3'], True),
    (['1', '2', '3'], ['1|2', '3|2'], False),
    (['1', '3', '2'], ['1|2', '3|2'], True),
    (['1', '3', '2', '4'], ['1|2', '3|2', '2|4', '3|4'], True),
])
def test_validate_update(update, rules, is_valid):
    rules_dict = rules_to_dictionary(rules)
    assert validate_update(update, rules_dict) == is_valid


def test_validate_update_sample():
    valid_updates = []
    rules, updates = parse_input(SAMPLE_INPUT)
    rules_dict = rules_to_dictionary(rules)
    for update in updates:
        if validate_update(update, rules_dict):
            valid_updates.append(update)

    assert valid_updates == [
        ['75', '47', '61', '53', '29'],
        ['97', '61', '53', '29', '13'],
        ['75', '29', '13'],
    ]
