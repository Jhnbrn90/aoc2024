from solution_2 import move_file_in_blocks


# SAMPLE_INPUT = '00...111...2...333.44.5555.6666.777.888899'


def test_move_file_in_block():
    # input_block = list(SAMPLE_INPUT)
    input_block = ['0', '0', '9', '9', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '.', '.']
    expected = list('00992111777.44.333....5555.6666.....8888..')

    move_file_in_blocks(input_block) 

    assert move_file_in_blocks == expected

