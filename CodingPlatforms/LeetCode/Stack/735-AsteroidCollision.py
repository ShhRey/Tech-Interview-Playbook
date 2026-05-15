# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


from typing import List

# Stack based Approach
# TC: O(N)       SC: O(N)
def asteroidCollision(asteroids: List[int]) -> List[int]:
    # Storing res
    stack = []
    # Iterate through the arr
    for a in asteroids:
        # Keep Checking until Collision Possiblity
        while stack and a < 0 and stack[-1] > 0:
            # Collisiion occurs with bigger Ast
            if abs(a) > stack[-1]:
                # Remove top
                stack.pop()
                # Keep Checking
                continue
            # Collision occurs with same Ast
            elif abs(a) == stack[-1]:
                stack.pop()
            # Curr Ast does not exist
            break
        # No Collision / Destroyed others
        else:
            # Add curr Ast to res
            stack.append(a)
    # Return all surviving asteroids
    return stack





# Custom Test Cases
q = asteroidCollision([10, 2, -5])
print(q)