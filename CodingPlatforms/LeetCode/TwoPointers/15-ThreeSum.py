# Question: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List


# Brute Force Approach   
# TC: O(N^3)  SC: O(N)
def threeSumBF(nums: List[int]) -> List[List[int]]:
    # Gathering non-dupl triplets
    res = set()
    # Iterating for first num
    for i in range(len(nums)):
        # Iterating for second num
        for j in range(i+1, len(nums)):
            # Iterating for third num
            for k in range(j+1, len(nums)):
                # Match all triplet conditions specified
                if nums[i] + nums[j] + nums[k] == 0:
                    # Form triplet of three nums as sorted tuple
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    # List all triplets from res
    return [list(triplet) for triplet in res]



# HashSet based Approach
# TC: O(N^2)       SC: O(N)
def threeSumHS(nums: List[int]) -> List[List[int]]:
    # Gathering non-dupl triplets
    res = set()
    # Iterating for first num
    for i in range(len(nums)):
        seen = set()
        # Iterating for second num
        for j in range(i+1, len(nums)):
            # Third num is -ve first and second
            comp = -nums[i] - nums[j]
            # Check for combinations
            if comp in seen:
                # Form triplets and add to result
                res.add(tuple(sorted([nums[i], nums[j], comp])))
            # Add to seen, diff combinations
            seen.add(nums[j])
    # List all triplets from res
    return [list(triplet) for triplet in res]



# 2Ptr based Approach   
# TC: O(N^2)  SC: O(1)
def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    # Gathering Duplicates
    nums.sort()
    # Iterating through nums
    for i, num in enumerate(nums):
        # Ignoring Duplicates, Moving ahead
        if i > 0 and num == nums[i-1]:
            continue
        # Creating var for 2Ptr
        l, r = i+1, len(nums)-1
        # Until left does not pass right
        while l < r:
            # Save the total of current triplet
            tot = num + nums[l] + nums[r]
            # Total less than 0, need bigger num
            if tot < 0:
                l += 1
            # Total more than 0, need smaller num
            elif tot > 0:
                r -= 1
            # Equal to Zero
            else:
                # Add triplets to result
                res.append([num, nums[l], nums[r]])
                l += 1
                r -= 1
                # Skipping Duplicates for l, r
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
    # List down all triplets
    return res





# Custom Test Cases
q = threeSum([-1,0,1,2,-1,-4])
print(q)