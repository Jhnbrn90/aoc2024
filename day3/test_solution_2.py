from solution_2 import extract_valid_multiplication_instructions


with open('day3/sample_2.txt') as f:
    SAMPLE_INPUT = f.read()


def test_it_extracts_do_multiplications():
    """Check that the input can be trimmed to only include valid instructions."""
    raw_instructions = extract_valid_multiplication_instructions(SAMPLE_INPUT)
    assert raw_instructions == "mul(2,4)mul(8,5)"