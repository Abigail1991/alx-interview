#!/usr/bin/python3
import sys
"""nqueens backtracking algorithm"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list (of coordinates)
    board = []
    for k in range(n):
        board.append([k, None])

    def is_safe(a, b):
        """determines if position (a, b) is safe"""

        # Check current row
        for l in range(n):
            if b == board[l][1]:
                return False

        # Check diagonals
        k = 0
        while(k < a):
            if abs(board[k][1] - b) == abs(k - a):
                return False
            k += 1
        # Position is safe!
        return True

    def solve(a):
        """solves and backtracks when encountering conflicts"""
        # loop through cols
        for b in range(n):
            # clear column
            for k in range(a, n):
                board[k][1] = None

            # checks if pos is safe (current col b + a row)
            if is_safe(a, b):
                board[a][1] = b
                # accept and print if we have the final # of queens
                if (a == n - 1):
                    print(board)
                # move to next column if not
                else:
                    solve(a + 1)

    # start the recursive process at a = 0
    solve(0)
