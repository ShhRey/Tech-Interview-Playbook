# Question: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# - Each row must contain the digits 1-9 without repetition.
# - Each column must contain the digits 1-9 without repetition.
# - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need to be validated according to the mentioned rules.

from typing import List
from collections import defaultdict


# Brute Force Approach   
# TC: O(9^3)        SC: O(1)
def isValidSudokuBF(board: List[List[str]]) -> bool:
    # Iterate through rows
    for r in range(9):
        # Iterate through cols
        for c in range(9):
            # If cell-val == . continue
            if board[r][c] == ".":
                continue
            # Store val of cell
            val = board[r][c]
            # Check for val in rows
            for i in range(9):
                # Check for dupl val in each row
                if i != r and board[i][c] == val:
                    return False
            # Check for val in cols
            for j in range(9):
                # Check for dupl val in each col
                if j != c and board[r][j] == val:
                    return False
            # Check for boxes
            boxR = (r // 3) * 3
            boxC = (c // 3) * 3
            # Iterate through these boxes
            for i in range(boxR, boxR+3):
                for j in range(boxC, boxC+3):
                    # Check for dupl in boxes along with RC check
                    if (i != r or j != c) and (board[i][j] == val):
                        return False
    # If no dupl found
    return True
            
            

# Multi-Set based Approach
# TC: O(9^2)       SC: O(1)
def isValidSudokuDD(board: List[List[str]]) -> bool:
    # Create DDs to store cells
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)
    # Iterate through the board
    for r in range(9):
        for c in range(9):
            # Store val of cell
            val = board[r][c]
            # Ignore if val is .
            if val == ".":
                continue
            # Check for dupl in rows
            if val in rows[r]:
                return False
            # Check for dupl in cols
            if val in cols[c]:
                return False
            # Create box as per size
            box = (r // 3, c // 3)
            # Check for dupl in box
            if val in boxes[box]:
                return False
            # Add cell val if no dupl
            rows[r].add(val)
            cols[c].add(val)
            boxes[box].add(val)
    # If no dupl found
    return True



# Single-Set based Approach
# TC: O(9^2)        SC: O(1)
def isValidSudoku1S(board: List[List[str]]) -> bool:
    # Set for visited cells
    seen = set()
    # Iterate through the board
    for r in range(9):
        for c in range(9):
            # Store val of cell
            val = board[r][c]
            # Ignore if val is .
            if val == ".":
                continue
            # Create tuple of val, cell dimensions
            row = (val, "row", r)
            col = (val, "col", c)
            box = (val, "box", r // 3, c // 3)
            # Check if dim already in set, return
            if row in seen or col in seen or box in seen:
                return False
            # Add dim once visited
            seen.add(row)
            seen.add(col)
            seen.add(box)
    # If no dupl found
    return True





# Custom Test Cases
q = isValidSudoku1S([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ])
print(q)