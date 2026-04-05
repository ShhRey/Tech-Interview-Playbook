# Question: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.


from typing import List


# Brute Force Approach   
# TC: O(m*n)  SC: O(1)
def searchBF(nums: List[int], target: int) -> int:
    # Iterate through the nums arr
    for i in range(len(nums)):
        # Check if any num = target
        if nums[i] == target:
            # Return match idx
            return i
    # Target not Found
    return -1



# Brute Force Approach   
# TC: O(m*n)  SC: O(1)
def search(nums: List[int], target: int) -> int:
    # Ptrs for BS Logic
    l, r = 0, len(nums)
    # Keep checking until condition
    while l <= r:
        # Set mid to l+r // 2
        m = (l+r) // 2
        # Return idx if num[mid] = target
        if nums[m] == target:
            return m
        # Target greater than mid, update left
        if nums[m] < target:
            l = m + 1
        # Target lesser than mid, update right
        else:
            r = m - 1
    # Target not Found
    return -1





# Custom Test Cases
q = search([-1,0,3,5,9,12], 3)
print(q)