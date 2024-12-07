from solution_1 import validate_update, parse_input, rules_to_dictionary


def correctly_order_update_line(update: list[str], rules_dict: dict) -> list[str]:
    while not validate_update(update, rules_dict):
        seen = []
        for page_number in update:
            if any(number in rules_dict[page_number] for number in seen):
                # Found a "after" number *before* the page_number
                idx = update.index(page_number)
                update[idx], update[idx-1] = update[idx-1], update[idx]
            seen.append(page_number)
    return update


def main():
    with open('day5/input_1.txt') as f:
        puzzle_input = f.read()

    rules, updates = parse_input(puzzle_input)
    rules_dict = rules_to_dictionary(rules)
    incorrect_updates = [u for u in updates if not validate_update(u, rules_dict)]

    middle_values = []
    for update in incorrect_updates:
        print(f"Incorrect update: {update}")
        fixed_update = correctly_order_update_line(update, rules_dict)
        middle_values.append(int(fixed_update[len(fixed_update) // 2]))
        print(f"Fixed updated: {fixed_update}")

    print(f"Sum of middle values: {sum(middle_values)}.")


if __name__ == "__main__":
      main()
