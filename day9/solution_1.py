def disk_map_to_block(disk_map: str) -> list[str]:
    """Parse disk map to block representation."""
    disk_map_list = list(disk_map.strip())
    block_representation = []

    file_id = 0
    for idx, digit in enumerate(disk_map_list):
        if idx % 2 == 0:  # file block
            value = str(file_id)
            file_id += 1
        else:  # free space
            value = '.'

        for _ in range(int(digit)):
            block_representation.append(value)

    return block_representation


def compact_block(block_input_list: list[str]) -> list[str]:
    """Compact block by moving right-most items to left-most free space.

    Initializing two pointers:
     - left pointer: start from beginning and search for free space
     - right pointer: start from end and search for file blocks
     """
    # Start free space search at left
    left = 0
    # Start finding file blocks from the right
    right = len(block_input_list) - 1

    while True:
        # Get the left most free space
        while block_input_list[left] != '.':
            left += 1

        # Get the right-most file block
        while block_input_list[right] == '.':
            right -= 1

        # When the left pointer can't find a free space
        # *before* the next file block, we've reached the end
        if left > right:
            break

        # Swap values
        block_input_list[left], block_input_list[right] = block_input_list[right], block_input_list[left]

    return block_input_list


def calculate_checksum(compressed_input: list[str]) -> int:
    """Calculate checksum for given compressed input.

    Multiply position with file_id for each entry.
    For example:
    [1, 3, 4] results in:
      - 0 * 1
      - 1 * 3
      - 2 * 4
    """
    checksum = 0
    for idx, file_id in enumerate(compressed_input):
        if file_id != '.':
            checksum += idx * int(file_id)
    return checksum


def main():
    with open('day9/input_1.txt') as f:
        puzzle_input = f.read().strip()

    block = disk_map_to_block(puzzle_input)
    compressed_block = compact_block(block)
    checksum = calculate_checksum(compressed_block)

    print(f"{checksum}")

if __name__ == "__main__":
    main()
