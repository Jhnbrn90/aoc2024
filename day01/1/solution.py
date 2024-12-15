from collections import defaultdict


def string_to_list(list_input: str, separator:str = "  ") -> list[list[int]]:
    """Convert the puzzle string input to their corresponding lists."""
    # Parse the input first by line, skipping empty lines
    rows = [row for row in list_input.split('\n') if row != '']

    # The rows are separated by a separator into columns, which
    # need to be temporarily stored. A default dict of lists was
    # choosen to easily group the columns of given length into their
    # corresponding "horizontal" list instead of their "vertical" list
    # representation.
    matrix: dict[int, list[int]] = defaultdict(list)
    for row in rows:
        columns = row.split(separator)

        # Dynamically add all columns to their corresponding
        # list based on the index within the default dict.
        for idx in range(len(columns)):
            # If the column has `n` values, the first is stored within a
            # list at idx=0, the second at idx=1, up util idx=n-1.
            matrix[idx].append(int(columns[idx]))

    # Since we're not interested in the actual index (only used for grouping),
    # the values are returned as a list of lists.
    return list(matrix.values())


def calculate_distance(list_input: list[list[int]]) -> list[int]:
    """Calculate the absolute difference between values within given lists."""
    zipped = zip(*list_input)
    return [abs(i-j) for i, j in zipped]


def main():
    with open('day01/1/input.txt') as f:
        puzzle_input = f.read()

    lists_of_ints = string_to_list(puzzle_input)
    # To get the difference between the minimum values of each list
    # first order the list by smallest ints.
    ordered_list_of_ints = [sorted(location_list) for location_list in lists_of_ints]

    distances = calculate_distance(ordered_list_of_ints)
    print(distances)

    print(f"Sum of distances: {sum(distances)}")


if __name__ == "__main__":
    main()
