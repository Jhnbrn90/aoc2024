from collections import defaultdict

def main():
    with open('day11/input_1.txt') as f:
        puzzle_input = f.read().strip()

    # stone_list = [int(stone) for stone in puzzle_input.split(' ')]
    stone_list = {int(stone): 1 for stone in puzzle_input.split(' ')}

    for blink in range(1,76):
        print(f"Calculating blink {blink}")
        new_stone_list = defaultdict(int)
        # for idx, stone in enumerate(stone_list):
        for stone, count in stone_list.items():
            if stone == 0:
                # new_stone_list.append(1)
                new_stone_list[1] += count
                continue
            if len(str(stone)) % 2 == 0:
                # Split the stone
                middle = len(str(stone))//2
                # Handle leading zero's
                first_half = int(str(stone)[:middle])
                second_half = int(str(stone)[middle:])
                # new_stone_list.append(first_half)
                # new_stone_list.append(second_half)
                new_stone_list[first_half] += count
                new_stone_list[second_half] += count
                continue
            new_stone_list[stone * 2024] += count

        stone_list = new_stone_list

        if blink == 25:
            print(sum(stone_list.values()))

        if blink == 75:
            print(sum(stone_list.values()))

    print("Done")


if __name__ == "__main__":
    main()