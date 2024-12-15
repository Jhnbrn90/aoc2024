from solution_2 import (
    calculate_checksum,
    disk_map_to_allocated_memory,
    move_file_blocks,
)

with open('day09/sample_1.txt') as f:
    SAMPLE_INPUT = f.read().strip()


def test_move_file_in_block():
    file_blocks, free_space = disk_map_to_allocated_memory(SAMPLE_INPUT)
    reordered_blocks = move_file_blocks(file_blocks, free_space)
    checksum = calculate_checksum(reordered_blocks)
    assert checksum == 2858
