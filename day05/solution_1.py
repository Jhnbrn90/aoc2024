from collections import defaultdict


def parse_input(puzzle_input: str):
    rule_lines, update_lines = puzzle_input.strip().split('\n\n')

    rules = rule_lines.split('\n')
    updates = [update.split(",") for update in update_lines.split('\n')]

    return rules, updates


def rules_to_dictionary(rules: list) -> dict:
    """Convert list of rules to dictionary of sets.
    
    "1": {"2", "3", "4"},
    "2": {"5", "6"},
    etc.

    The numbers in the set must come after the key.
    """
    rule_dict = defaultdict(set)
    for rule in rules:
        x, y = rule.strip().split("|")
        rule_dict[x].add(y)

    return rule_dict


def validate_update(update: list, rules_dict: dict) -> bool:
    """Loop over update list and check if it adheres to the rules."""
    seen_page_numbers = set()

    for page_number in update:
        # Check if the page numbers *after* `page_number`
        # have been seen yet. If so, they were *before* the
        # actual 
        if rules_dict[page_number].intersection(seen_page_numbers):
            return False
        
        # The page was not seen yet, add it to the set of seen pages
        seen_page_numbers.add(page_number)

    # All page_numbers stood the test and so this update adheres to the rules
    return True


def main():
    with open('day05/sample_1.txt') as f:
        puzzle_input = f.read()

    rules, updates = parse_input(puzzle_input)
    rules_dict = rules_to_dictionary(rules)

    total_sum = 0
    for update in updates:
        if validate_update(update, rules_dict):
            # Get the middle value
            middle_value = update[len(update) // 2]
            total_sum += int(middle_value)

    print(f"Total sum: {total_sum}")


if __name__ == "__main__":
    main()
