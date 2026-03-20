# Question: Return True if any value in an integer array appears twice and return False if every value is distinct

from typing import List


# Brute Force Approach
# TC: O(N^2)    SC: O(1)
def containsDuplicateBF(nums: List[int]) -> bool:
    # Consider one number and iterate
    for i in range(len(nums)):
        # Consider second number and iterate
        for j in range(i+1, len(nums)):
            # Check if Numbers Equal
            if nums[i] == nums[j]:
                return True
    return False



# Sorting based Approach
# TC: O(Nlogn)    SC: O(1)
def containsDuplicateS(nums: List[int]) -> bool:
    # Sorting brings duplicates together
    nums.sort()
    # Iterate through nums from idx 1
    for i in range(1, len(nums)):
        # Check Num at prev-idx
        if nums[i] == nums[i-1]:
            return True
    return False



# Set-based Approach
# TC: O(N)    SC: O(N)
def containsDuplicate(nums: List[int]) -> bool:
    # Initialize a Set
    numSet = set()
    # Check for every Num
    for num in nums:
        # If already in Set
        if num in numSet:
            return True
        # If not, add in Set
        else:
            numSet.add(num)
    return False


# One-line Set Approach          
# TC: O(N)      SC: O(N)
def containsDuplicate2(nums: List[int])-> bool:
    return len(nums) == len(set(nums))





# Custom Test Cases
q = containsDuplicate([1,2,3,1])
print(q)