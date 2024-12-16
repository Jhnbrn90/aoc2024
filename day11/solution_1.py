def normalise_zeros(number: str) -> str:
    """Remove leading zero's from string."""
    return str(int(number))


def blink(initial: str) -> str:
    """Perform the `blink` operation using the given rules."""
    stones = initial.strip().split(' ')
    new_stones = []

    for stone in stones:
        if stone == '0':
            new_stones.append('1')
            continue
        if len(stone) % 2 == 0:
            # Split the stone
            middle = len(stone)//2
            # Handle leading zero's
            first_half = normalise_zeros(stone[:middle])
            second_half = normalise_zeros(stone[middle:])
            new_stones.append(first_half)
            new_stones.append(second_half)
            continue
        # None of the other rules apply
        new_stone = int(stone) * 2024
        new_stones.append(str(new_stone))

    return " ".join(new_stones)


def count_stones(stones: str) -> int:
    """Return total amount of stones in line."""
    return len(stones.strip().split(' '))


def perform_blinks(initial_arrangement: str, blink_count: int) -> str:
    """Perform the `blink` action for a given number of times using an initial setup."""
    stones = initial_arrangement
    for _ in range(blink_count):
        stones = blink(stones)
    return stones


def main():
    with open('day11/input_1.txt') as f:
        initial_arrangement = f.read().strip()

    blink_count = 25

    stones = perform_blinks(initial_arrangement, blink_count)
    total = count_stones(stones)

    print(f"Number of stones: {total}")

if __name__ == "__main__":
    main()