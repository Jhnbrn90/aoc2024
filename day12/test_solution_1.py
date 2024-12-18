from solution_1 import get_perimeter


with open('day12/sample_1.txt') as f:
    SAMPLE_INPUT = f.read()



def test_get_perimeter():
    """Check the perimeter is obtained for a garden plot.
    
        0  1  2  3
        _
    0  |A| _
    1  |A  A|
    2   -  -
    3

    For the coordinates (x, y) => A
        x  y 
     - (0, 0)
     - (0, 1)
     - (1, 1)

    The perimeter is 8.
    """
    garden_plot = {
        (0, 0),
        (1, 0),
        (1, 1),
    }

    assert get_perimeter(garden_plot) == 8
