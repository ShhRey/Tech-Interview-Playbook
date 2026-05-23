# Question: There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.


from typing import List

# Binary Search based Approach
# TC: O(N)       SC: O(1)
def search(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums)-1
    # BS Condition
    while l <= r:
        # Define mid element
        m = l+(r-l) // 2
        # Cond1: mid is target
        if nums[m] == target:
            return True
        # Cond2: duplicate val at all idx
        if nums[l] == nums[m] == nums[r]:
            # Upd ptrs
            l += 1
            r -= 1
        # left side is sorted
        if nums[l] <= nums[m]:
            # target betwn left (inc) and mid
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        # right side is sorted
        else:
            # target betwn mid and right (inc)
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    # Target not found
    return False





# Custom Test Cases
q = search([2,5,6,0,0,1,2], 0)
print(q)