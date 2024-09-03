"""
Description:

You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
"""

from collections import defaultdict

def validSudoku(Sudoku):
    blocks = defaultdict(set)
    # A sudoku is 9x9
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            block_idx = (i//3, j//3)
            # Check all the row
            if Sudoku[i][j] in row or Sudoku[j][i] in col or Sudoku[i][j] in blocks[block_idx]:
                return False
            # Empty cell
            if Sudoku[i][j] != ".":
                row.add(Sudoku[i][j])
                blocks[block_idx].add(Sudoku[i][j]) 
            if Sudoku[j][i] != ".":
                col.add(Sudoku[j][i])

    return True

if __name__ == "__main__":
    Sudoku = []
    for i in range(9):
        row = input()
        row = row.split()
        Sudoku.append(row)

    result = validSudoku(Sudoku)
    print(result)
