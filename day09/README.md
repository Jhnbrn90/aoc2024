# Puzzle instructions


(1) 
Disk map

file|free|file|free|etc...

12345 --> 1|2|3|4|5

1-block file
2-block free
3-block file
4-block free
5-block file

909090 --> 3 x 9-block file with no (0) free space.

(2)
Each file has an ID, starting from left id = 0.

In 12345:
- ID 0 = 1-block file
- ID 1 = 3-block file
- ID 2 = 5-block file

(3)
representation: 0..111....22222

(4)
Move file blocks from end to fill up empty space on left

0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......

(5)
checksum

Multiply position (index) with file ID it contains

For `0099811188827773336446555566..............`:
    - 0 * 0
    - 1 * 0
    - 2 * 9
    - 3 * 9
    - 4 * 8
    - etc.
sample calculates to 1928.
