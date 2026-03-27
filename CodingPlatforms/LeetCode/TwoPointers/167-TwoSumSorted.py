# Question: Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# Your solution must use only constant extra space.

from typing import List


# Brute Force Approach   
# TC: O(N^2)  SC: O(1)
def twoSumBF(numbers: List[int], target: int) -> List[int]:
    # Iterate through arr for num1
    for i in range(len(numbers)):
        # Iterate through arr for num2
        for j in range(i+1, len(numbers)):
            # Check if num1+num2 = target or not
            if numbers[i] + numbers[j] == target:
                # Return idx+1 for both
                return [i+1, j+1]


# 2Ptr based Approach   
# TC: O(N)  SC: O(1)
def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while l < r:
        # Store curr tot and compare with target
        total = numbers[l] + numbers[r]
        # tot = target, return res
        if total == target:
            return [l+1, r+1]
        # tot < target, inc left
        elif total < target:
            l += 1
        # tot > target, dec right
        else:
            r -= 1


# Custom Test Cases
q = twoSumBF([2,3,4], 6)
print(q)