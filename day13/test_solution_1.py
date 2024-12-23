from solution_1 import (
    Button,
    Machine,
    Prize,
    calculate_button_presses,
)


def test_calculate_button_presses():
    a = Button(x=94, y=34)
    b = Button(x=22, y=67)
    prize = Prize(x=8400, y=5400)

    machine = Machine(a, b, prize)

    assert calculate_button_presses(machine) == {
        "A": 80,
        "B": 40,
    }


def test_parse_input_to_machines():
    machine_definition = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
"""
    assert Machine.from_str(machine_definition) == Machine(
        button_a=Button(x=94, y=34),
        button_b=Button(x=22, y=67),
        prize=Prize(x=8400, y=5400)
    )

