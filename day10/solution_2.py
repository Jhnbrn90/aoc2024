from collections import namedtuple


HikingStep = namedtuple('HikingStep', ['height', 'x', 'y'])

DIRECTIONS_YX = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
)


def parse_input_to_grid(puzzle_input: str) -> list[list[str]]:
    return [list(e) for e in puzzle_input.strip().split('\n')]


def get_trailheads(grid: list[list[str]]) -> list[tuple]:
    trailheads = []

    rows = len(grid)
    columns = len(grid[0])

    for y in range(rows):
        for x in range(columns):
            height = int(grid[y][x])
            if height == 0:
                trailheads.append(
                    HikingStep(height, x, y)
                )

    return trailheads


def walk_trail(step: HikingStep, grid: list[list[str]]):
    if step.height == 9:
        # We've found the highest point / endpoint of our trail
        return 1

    score = 0
    for dy, dx in DIRECTIONS_YX:
        # For every neighbour, check if we should follow the path further
        x = step.x + dx
        y = step.y + dy

        if not(0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            # Bail out if the neighbour coordinates are not within the grid
            continue

        height = int(grid[y][x])
        if height == step.height + 1:
            # Continue traversal for the next hiking step
            next_step = HikingStep(height, x, y)
            score += walk_trail(next_step, grid)

    return score


def main():
    with open(f'day10/input_1.txt') as f:
        puzzle_input = f.read()

    scores = []
    grid = parse_input_to_grid(puzzle_input)
    trail_heads = get_trailheads(grid)

    for trail_head in trail_heads:
        scores.append(walk_trail(step=trail_head, grid=grid))

    print(f"Scores: {sum(scores)}")


if __name__ == "__main__":
    main()
