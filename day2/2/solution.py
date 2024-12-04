def get_levels_from_input(puzzle_input: str) -> list[list[int]]:
    """Parse input reports to levels."""
    # Remove extra newlines and then split entries on newline
    reports = puzzle_input.rstrip('\n').split('\n')
    levels: list[list[str]] = [report.split(' ') for report in reports]
    levels_int: list[list[int]] = [list(map(int, level)) for level in levels]

    return levels_int


def damper(level: list[int]) -> bool:
    """Check damping a value in the level."""
    for i in range(len(level)):
        if level_is_safe(level[:i] + level[i+1:], dampered=True):
            return True

    return False


def level_is_safe(level: list[int], dampered=False) -> bool:
    """Determine if a given level is safe."""
    # Use first two entries to determine if the level is ascending
    ascending_mode = level[1] > level[0]

    for i in range(len(level)-1):  # range is exclusive of end
        current_level = level[i]
        next_level = level[i+1]
        is_ascending = next_level > current_level

        if not (1 <= abs(current_level-next_level) <= 3):
            if not dampered:
                print(f"Considered level unsafe: {level}, damping...")
                return damper(level)
            else:
                print(f"Considered level unsafe: {level}. Reason: RANGE.")
                return False

        if (ascending_mode and not is_ascending) or (not ascending_mode and is_ascending):
            # Failed level, but we might get it working with a damped value
            if not dampered:
                print(f"Considered level unsafe: {level}, damping...")
                return damper(level)
            else:
                print(f"Considered level unsafe: {level}. Reason: ASC/DESC mixed.")
                return False
    else:
        print(f"Considered level safe: {level}")
        return True


def main():
    with open('day2/2/input.txt') as f:
        puzzle_input = f.read()

    safe_levels = 0
    levels = get_levels_from_input(puzzle_input)

    for level in levels:
        if level_is_safe(level):
            safe_levels += 1

    print(f"Number of safe levels: {safe_levels}")
    


if __name__ == "__main__":
    main()
