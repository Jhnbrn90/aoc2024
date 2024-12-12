from dataclasses import dataclass


@dataclass
class FileBlock:
    file_id: int
    start: int
    size: int


@dataclass
class FreeBlock:
    start: int
    size: int


def disk_map_to_allocated_memory(disk_map: str):
    file_blocks = []
    free_space = []

    start = 0
    file_id = 0
    for i in range(len(disk_map)):
        block_size = int(disk_map[i])
        if i % 2 == 0:
            file_blocks.append(FileBlock(
                file_id=file_id,
                start=start,
                size=block_size
            ))
            file_id += 1
        else:
            free_space.append(FreeBlock(start=start, size=block_size))

        start += block_size

    return file_blocks, free_space


def move_file_blocks(file_blocks, free_space):
    reordered_blocks = []

    for file_block in reversed(file_blocks):
        for free_block in free_space:
            # Loop over possible free spaces to contain this file block
            if free_block.start < file_block.start and free_block.size >= file_block.size:
                # Move the current file to the `free_start` index 
                file_block.start = free_block.start

                # Update the remaining free space
                free_block.start += file_block.size  # start position of the free block
                free_block.size -= file_block.size  # size of the free block is corrected
                break

        reordered_blocks.append(file_block)

    return reordered_blocks


def calculate_checksum(blocks):
    checksum = 0

    for file_block in blocks:
        start = file_block.start
        size = file_block.size

        for idx in range(start, start+size):
            # If the file_id covers 3 places, count 3 places
            # up from `start` index to account for `index * file ID`.
            checksum += file_block.file_id * idx

    return checksum


def main():
    with open('day9/input_1.txt') as f:
        puzzle_input = f.read().strip()

    file_blocks, free_space = disk_map_to_allocated_memory(puzzle_input)
    reordered_blocks = move_file_blocks(file_blocks, free_space)

    checksum = calculate_checksum(reordered_blocks)
    print(f'Checksum: {checksum}')


if __name__ == "__main__":
    main()
