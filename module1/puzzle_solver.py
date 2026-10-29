import sys
import random
from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# possible to enforce specific initial state through command line
# read from a file or use command line parameters

# display the first solution

# dict of {number: position}

# make a board instead of a list (goes through 0,3,6 rows)
def print_board(board):
    for i in range(0, 9, 3):
        print(*board[i:i + 3])


# counts inversions, how many times a larger number is in front of the smaller one, not including 0
# the number has to be even for the puzzzle to be solvable
def is_solvable(board):
    inversions = 0

    for i in range(9):
        for j in range(i + 1, 9):
            if board[i] != 0 and board[j] != 0:
                if board[i] > board[j]:
                    inversions += 1

    return inversions % 2 == 0


def generate_puzzle():
    board = list(GOAL)

    while True:
        random.shuffle(board)

        if is_solvable(board) and tuple(board) != GOAL:
            return tuple(board)


# find the 0 field, calculate where it is placed (row,column)
def get_neighbors(board):
    zero = board.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        # doesn't allow to go outside of the board
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col

            new_board = list(board)

            new_board[zero], new_board[new_pos] = (
                new_board[new_pos], new_board[zero]
            )

            yield tuple(new_board)



def main():
    if len(sys.argv) != 2:
        print("Usage: puzzle_solver <file_name>", file=sys.stderr)
        return

    with open(sys.argv[1], 'r') as file:
        data = file.read()

    # Convert file content into integers
    numbers = [int(x) for x in data.split()]

    # Check if numbers are valid
    if sorted(numbers) != list(range(9)):
        print("Invalid numbers", file=sys.stderr)
        sys.exit(1)

    # Create dict: number -> position
    positions = {}

    for index, number in enumerate(numbers):
        positions[number] = index

    print(positions)


if __name__ == "__main__":
    main()