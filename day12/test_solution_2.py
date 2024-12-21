from solution_2 import get_sides



def test_get_sides_for_garden_plot():
    """Check the sides are calculated for a garden plot.
    
    
         0  1  2  3
         __________
    0  | A  A  A  A | 
    1    __________  
    2
    3

    For the coordinates (x, y) => A
        x  y 
     - (0, 0)
     - (1, 0)
     - (2, 0)
     - (3, 0)

    The number of sides is 4.
    """
    garden_plot = {
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
    }

    assert get_sides(garden_plot) == 4
