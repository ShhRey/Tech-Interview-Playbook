# Question: Given the array nums, after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


from typing import List

# Binary Search based Approach   
# TC: O(log(N))  SC: O(1)
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    # BS Condition but l <= r
    while l <= r:
        # Define mid element
        m = (l + r) // 2
        # mid is equal to target
        if nums[m] == target:
            return m
        # left side is sorted
        elif nums[l] <= nums[m]:
            # Find target between left and mid inc left
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        # right side is sorted
        else:
            # Find target between mid and right inc right
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    # Target not Found
    return -1





# Custom Test Cases
q = search([4,5,6,7,0,1,2], 2)
print(q)