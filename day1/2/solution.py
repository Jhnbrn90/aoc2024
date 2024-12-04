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


def get_similarity_scores(lists_input: list[list[int]]) -> list[int]:
    similarity_scores = []

    for entry in lists_input[0]:
        entry_count = lists_input[1].count(entry)
        similarity_scores.append(entry_count*entry)
    return similarity_scores


def main():
    with open('day1/2/input.txt') as f:
        puzzle_input = f.read()

    lists_input = string_to_list(puzzle_input)
    similarity_scores = get_similarity_scores(lists_input)

    print(f'Sum of similarity scores: {sum(similarity_scores)}')

if __name__ == "__main__":
    main()
