#!/usr/bin/python3
"""Solves the N queens puzzle."""
import sys


def is_safe(board, row, col):
    """Checks if a queen can be placed at (row, col) safely.

    Args:
        board: list where board[i] is the column of the queen in row i.
        row: the row to check.
        col: the column to check.

    Returns:
        True if placing a queen at (row, col) is safe, False otherwise.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n):
    """Solves the N queens puzzle and prints every solution.

    Args:
        n: the size of the board (n x n) and number of queens.
    """
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solution = [[r, board[r]] for r in range(n)]
            print(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
