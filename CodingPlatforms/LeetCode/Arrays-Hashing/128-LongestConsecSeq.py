# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

from typing import List


# Brute Force Approach   
# TC: O(N^2)  SC: O(1)
def longestConsecutiveBF(nums: List[int]) -> int:
    # Initialize Max Count = 0
    res = 0
    # Iterate nums arr
    for num in nums:
        # Set curr = first num
        curr = num
        # res len to 1
        nlen = 1
        # Keep checking for curr+1
        while curr+1 in nums:
            # Update curr, res len
            curr += 1
            nlen += 1
        # Compare res and res len
        res = max(res, nlen)
    # Return res
    return res



# Sorting based Approach
# TC: O(nlogn)      SC: O(1)
def longestConsecutiveS(nums: List[int]) -> int:
    # Check for arr
    if not nums:
        return 0
    # Convert arr to set and sort
    nums = sorted(set(nums))
    # Initialize curr, nlen
    curr, nlen = 1, 1
    # Iterate nums arr for len
    for i in range(1, len(nums)):
        # Compare nums at i and i-1
        if nums[i] == nums[i-1] + 1:
            curr += 1
        # When condition differs
        else:
            # Check for maxL, set curr = 1
            nlen = max(curr, nlen)
            curr = 1
    # Compare numL and return
    return max(curr, nlen)



# Set based Approach
# TC: O(N)      SC: O(N)
def longestConsecutive(nums: List[int]) -> int:
        # Convert list to set -> handles dupl
        nset = set(nums)
        res = 0
        # Iterate through set
        for num in nset:
            # num-1 not in set, series starting
            if num-1 not in nset:
                # curr = num, len = 1
                curr = num
                nlen = 1
                # Expand series if nxt-num found
                while curr+1 in nset:
                    curr += 1
                    nlen += 1
                # Update for longest series
                res = max(res, nlen)
        # Return count
        return res
  




# Custom Test Cases
q = longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(q)