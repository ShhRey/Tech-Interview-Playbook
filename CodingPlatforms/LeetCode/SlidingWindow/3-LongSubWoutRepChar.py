# Question: Given a string s, find the length of the longest substring without duplicate characters.


# Brute Force Approach   
# TC: O(N^2)  SC: O(N)
def lengthOfLongestSubstringBF(s: str) -> int:
    # Initialize maxL to 0
    maxL = 0
    # Iterate through str
    for i in range(len(s)):
        # Storing unique chars
        seen = set()
        # Second Ptr for checking maxL
        for j in range(i, len(s)):
            # Stop counting if in set
            if s[j] in seen:
                break
            # Add char in set
            seen.add(s[j])
            # Update the maxL by checking two ptrs
            maxL = max(maxL, j-i+1)
    # Return maxL
    return maxL



# Set-based 2Ptr Approach   
# TC: O(N)  SC: O(N)
def lengthOfLongestSubstring2P(s: str) -> int:
    # Storing unique chars 
    charSet = set()
    # Initialize var to 0
    l, maxL = 0, 0
    # Iterate through str for window
    for r in range(len(s)):
        # Keep checking if char in Set
        while s[r] in charSet:
            # Remove from left
            charSet.remove(s[l])
            # Move left boundary forward
            l += 1
        # Add uniq char to Set
        charSet.add(s[r])
        # Update maxL for the str
        maxL = max(maxL, r-l+1)
    # Return maxL
    return maxL



# HashMap based Approach
# TC: O(N)       SC: O(N)
def lengthOfLongestSubstring(s: str) -> int:
    # Map char with idx
    cmap = {}
    # Initialize var to 0
    l, maxL = 0, 0
    # Iterate through str for window
    for r in range(len(s)):
        # If char in Map
        if s[r] in cmap:
            # Move left boundary forward
            l = max(l, cmap[s[r]]+1)
        # Update idx of char in Map
        cmap[s[r]] = r
        # Update maxL for the str
        maxL = max(maxL, r-l+1)
    # Return maxL
    return maxL





# Custom Test Cases
q = lengthOfLongestSubstring('ababcabcda')
print(q)