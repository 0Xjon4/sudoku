import random
from sudoku import can_place, find_empty, EMPTY


def fill_grid(grid):
    """Fill the grid completely, trying digits in random order."""
    empty = find_empty(grid)

    if empty is None:
        return True

    row, col = empty

    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for num in numbers:
        if can_place(grid, row, col, num):
            grid[row][col] = num

            if fill_grid(grid):
                return True

            grid[row][col] = EMPTY

    return False
import copy

DIFFICULTY = {"easy": 35, "medium": 45, "hard": 52}


def make_puzzle(difficulty="medium"):
    """Return (puzzle, solution) for the given difficulty."""
    solution = [[0] * 9 for _ in range(9)]
    fill_grid(solution)

    puzzle = copy.deepcopy(solution)

    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    for r, c in positions[:DIFFICULTY[difficulty]]:
        puzzle[r][c] = EMPTY

    return puzzle, solution