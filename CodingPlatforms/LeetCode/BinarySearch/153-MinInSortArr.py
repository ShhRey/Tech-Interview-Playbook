# Question: Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

from typing import List

# Brute Force Approach   
# TC: O(N)  SC: O(1)
def findMin(nums: List[int]) -> int:
    min(nums)
 
# Binary Search Approach  
# TC: O(log(N))  SC: O(1)
def findMin(nums: List[int]) -> int:
    # Initialize left, right ptrs
    l, r = 0, len(nums) - 1
    # BS Condition
    while l < r:
        # Initialize mid to l+r //2
        m = (l+r) // 2
        # val at m greater than val at r
        if nums[m] > nums[r]:
            # Shift left ptr
            l = m + 1
        # val at m less than val at r
        else:
            # Shift right ptr
            r = m
    # When left==right, return nums[l]
    return nums[l]


# Custom Test Cases
q = findMin(3,4,5,1,2)
print(q)