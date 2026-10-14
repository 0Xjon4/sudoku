EMPTY = 0
def row_has(grid, row, num):
    """Return True if num already appears in the given row."""
    return num in grid[row]
def col_has(grid, col, num):
    """Return True if num already appears in the given column."""
    for row in range(9):
        if grid[row][col] == num:
            return True
    return False
def box_has(grid, row, col, num):
    """Return True if num already appears in the 3x3 box containing (row, col)."""
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return True
    return False
def can_place(grid, row, col, num):
    """Return True if num can legally be placed at (row, col)."""
    if row_has(grid, row, num):
        return False
    if col_has(grid, col, num):
        return False
    if box_has(grid, row, col, num):
        return False
    return True
def find_empty(grid):
    """Return (row, col) of the first empty cell, or None if the grid is full."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == EMPTY:
                return row, col
    return None
def solve(grid):
    """Solve the grid in place. Return True if solved, False if no solution."""
    empty = find_empty(grid)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if can_place(grid, row, col, num):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = EMPTY

    return False