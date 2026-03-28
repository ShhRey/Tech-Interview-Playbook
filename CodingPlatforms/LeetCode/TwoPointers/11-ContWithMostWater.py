# Question: Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

from typing import List

# Brute Force Approach   
# TC: O(N*2)  SC: O(1)
def maxAreaBF(height: List[int]) -> int:
    area = 0
    # Iterating for one dimension
    for i in range(len(height)):
        # Iterating for second dimension
        for j in range(i+1, len(height)):
            # Calculating area between two bars and maximizing res
            area = max(area, (j-i) * min(height[i], height[j]))
    # Return res
    return area



# 2Ptr Approach   
# TC: O(N)  SC: O(1)
def maxArea(height: List[int]) -> int:
    # create left and right pointers
    l, r = 0, len(height)-1
    res = 0
    # Keep checking until BS Condition
    while l < r:
        # Calculate area between two bars
        area = (r-l) * min(height[l], height[r])
        # Comparing area for maximizing res
        res = max(res, area)
        # check for bar heights and inc/dec
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    # Return max area
    return res




        
# Custom Test Cases
q = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(q)