from solution_1 import disk_map_to_block, compact_block, calculate_checksum

with open('day9/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()

def test_disk_map_to_block():
    block = disk_map_to_block(SAMPLE_INPUT)
    expected = list('00...111...2...333.44.5555.6666.777.888899')
    assert block == expected


def test_compact_block():
    block_input = list('00...111...2...333.44.5555.6666.777.888899')
    free_space_count = block_input.count('.')
    expected = list('0099811188827773336446555566' + '.' * free_space_count)
    assert compact_block(block_input) == expected


def test_calculate_checksum():
    compressed_input = '0099811188827773336446555566'
    expected_checksum = 1928
    assert calculate_checksum(compressed_input) == expected_checksum
