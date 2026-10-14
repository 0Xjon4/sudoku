import sys
import unittest

sys.path.append("backend")

from sudoku import row_has, col_has, box_has, can_place, solve


def empty_grid():
    return [[0] * 9 for _ in range(9)]


class TestRules(unittest.TestCase):

    def test_row_has(self):
        grid = empty_grid()
        grid[4][0] = 5
        self.assertTrue(row_has(grid, 4, 5))
        self.assertFalse(row_has(grid, 4, 7))
        self.assertFalse(row_has(grid, 3, 5))

    def test_col_has(self):
        grid = empty_grid()
        grid[7][2] = 4
        self.assertTrue(col_has(grid, 2, 4))
        self.assertFalse(col_has(grid, 3, 4))

    def test_box_has(self):
        grid = empty_grid()
        grid[3][6] = 8
        self.assertTrue(box_has(grid, 5, 7, 8))
        self.assertFalse(box_has(grid, 0, 0, 8))

    def test_can_place_blocked_by_row(self):
        grid = empty_grid()
        grid[0][0] = 5
        self.assertFalse(can_place(grid, 0, 8, 5))

    def test_can_place_allowed(self):
        grid = empty_grid()
        self.assertTrue(can_place(grid, 0, 0, 5))


class TestSolver(unittest.TestCase):

    def test_solves_empty_grid(self):
        grid = empty_grid()
        self.assertTrue(solve(grid))
        for row in grid:
            self.assertEqual(sorted(row), list(range(1, 10)))


if __name__ == "__main__":
    unittest.main()