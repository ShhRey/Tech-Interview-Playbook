# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

# Brute Force Approach   
# TC: O(N^2)  SC: O(1)
def productExceptSelfBF(nums: List[int]) -> List[int]:
    res = []
    # Iterating through the arr
    for i in range(len(nums)):
        prod = 1
        # Checking for diff index
        for j in range(len(nums)):
            # Prod only if diff
            if i != j:
                prod *= nums[j]
        # Append to res after inner loop
        res.append(prod)
    # Return res
    return res    



# Left + Right based Approach
# TC: O(N)      SC: O(N)
def productExceptSelfLR(nums: List[int]) -> List[int]:
    n = len(nums)
    # Creating dupl arrays
    left = [1] * n
    right = [1] * n
    # Final res
    res = []
    # Iterating nums arr to obtain desired res
    for i in range(1, n):
        # Store prod of num[i] with its left pos 
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        # Store prod of num[i] with its right pos
        right[i] = right[i+1] * nums[i+1]
    for i in range(n):
        # Combining and mult left and right arrs
        res.append(left[i] * right[i])
    # Returning final res
    return res



# Pre + Postfix based Approach
# TC: O(N)    SC: O(1)
def productExceptSelfPP(nums: List[int]) -> List[int]:
    # Arr: 1 for every idx
    res = [1] * len(nums)
    prefix = 1
    # Prefix Loop (front to back)
    for i in range(len(nums)):
        # Fetch curr-idx-num as prefix, multiply nums
        res[i] = prefix
        prefix *= nums[i]
    # Postfix Loop (back to front)
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        # Fetch curr-idx-res, multiply postfix
        res[i] *= postfix
        postfix *= nums[i]
    # Return res
    return res





# Custom Test Cases
q = productExceptSelfLR([1,2,3,4])
print(q)