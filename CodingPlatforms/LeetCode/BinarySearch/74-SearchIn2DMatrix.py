# Question: You are given an m x n integer matrix matrix with the following two properties:
'''
 - Each row is sorted in non-decreasing order.
 - The first integer of each row is greater than the last integer of the previous row.
'''
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

from typing import List


# Brute Force Approach   
# TC: O(m*n)  SC: O(1)
def searchMatrixBF(matrix: List[List[int]], target: int) -> bool:
    # Iterate matrix wrt Rows
    for r in range(len(matrix)):
        # Iterate matrix wrt Cols
        for c in range(len(matrix[0])):
            # Check every cell and comp with target
            if matrix[r][c] == target:
                # Target Found
                return True
    # If target not found
    return False



# Row-wise Binary Search Approach
# TC: O(m+logn)       SC: O(1)
def searchMatrixRBS(matrix: List[List[int]], target: int) -> bool:
    # Iterate matrix wrt Row
    for row in matrix:
        # Check if target in row, else skip row
        if row[0] <= target <= row[-1]:
            # Ptrs for Binary Search
            l, r = 0, len(row)-1
            while l <= r:
                # Initialize mid as l+r // 2
                m = (l+r) // 2
                # Check if row[mid] is target
                if row[m] == target:
                    return True
                # Target greater than mid
                elif row[m] < target:
                    l = m + 1
                # Target lesser than mid
                else:
                    r = m - 1
    # Target not Found
    return False
    


# Binary Search Approach   
# TC: O(log(m*n))  SC: O(1)
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # Define Dimensions for Matrix
    rows, cols = len(matrix), len(matrix[0])
    # Ptrs for BS across matrix
    l, r = 0, (rows*cols)-1
    while l <= r:
        # Define mid val
        m = (l+r) // 2
        # Define row and col wrt mid
        row = m // cols
        col = m % cols
        # Compare cell val with target
        if matrix[row][col] == target:
            return True
        # Target greater than cell val
        elif matrix[row][col] < target:
            l = m + 1
        # Target lesser than cell val
        else:
            r = m - 1
    # Target not Found
    return False




# Custom Test Cases
q = searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34)
print(q)