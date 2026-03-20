# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

from typing import List

# Brute Force Approach   
# TC: O(N^2)  SC: O(1)
def TwoSumBF(nums: List[int], target: int) -> List[int]:
    # Consider one number and iterate
    for i in range(len(nums)):
        # Consider other number and iterate
        for j in range(i+1, len(nums)):
            # Check if total == Target
            if nums[i] + nums[j] == target:
                # Return index
                return [i, j]
            


# Binary Search based Approach
# TC: O(Nlogn)      SC: O(N)
def TwoSumBS(nums: List[int], target: int) -> List[int]:
    # Attaching idx to nums
    arr = list(enumerate(nums))
    # Sorting wrt num
    arr.sort(key=lambda x:x[1])
    # Initiating BS var
    l, r = 0, len(nums)-1
    # Iterating through nums
    while l < r:
        # Calculate Sum of left + right
        s = arr[l][1] + arr[r][1]
        # If s == target, return idx
        if s == target:
            return [arr[l][0], arr[r][0]]
        # If s greater, inc left
        elif s < target:
            l += 1
        # If s less, dec right
        else:
            r -= 1



# 2. Hashmap Approach       
# TC: O(N)    SC: O(N)
def TwoSum(nums: List[int], target: int) -> List[int]:
    # Initialize map
    hmap = {}
    # Iterate using idx, num from nums
    for i, num in enumerate(nums):
        # Calc rem for each num
        rem = target - num
        # Check for rem in map
        if rem in hmap:
            # Ret idx-rem and idx-num
            return [hmap[rem], i]
        else:
            # Add num to map
            hmap[num] = i





# Custom Test Cases
q = TwoSum([3, 1, 2, 7, 9, 4], 6)
print(q)