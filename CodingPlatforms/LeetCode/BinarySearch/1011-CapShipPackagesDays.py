# Question: A conveyor belt has packages that must be shipped from one port to another within days days. The ith package on the conveyor belt has a weight of weights[i]. 
# Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
# It is not allowed to load weight more than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.


from typing import List

# Binary Search based Approach
# TC: O()       SC: O()
def shipWithinDays(self, weights: List[int], days: int) -> int:
    # Setting range from Max to Sum
    l, r = max(weights), sum(weights)
    # Defining res with the total and trying lower values
    res = r
    # Calc cap and num of days
    def helper(cap):
        # Def vals for ship and curr cap
        ship, curr = 1, cap
        # Check every weight
        for w in weights:
            # Cap for the day finishes
            if curr - w < 0:
                # Inc the ship count
                ship += 1
                # Reset the cap
                curr = cap
            # Keep reducing cap
            curr -= w
        return ship <= days
    # Binary Search condition
    while l <= r:
        # Set mid value
        m = (l+r) // 2
        # Check for cap
        if helper(m):
            # Compare min with res
            res = min(res, m)
            # Upd range
            r = m - 1
        else:
            # Upd range
            l = m + 1
    # Return the res
    return res