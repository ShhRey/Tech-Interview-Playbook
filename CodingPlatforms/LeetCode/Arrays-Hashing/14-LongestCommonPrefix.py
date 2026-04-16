# Question: Find the longest common prefix string amongst an array of strings, if nothing return ""

from typing import List

# Brute Force Approach   
# TC: O(N*M^2)  SC: O(1)
def longestCommonPrefixBF(strs: List[str]) -> str:
    # No words in strs
    if not strs:
        return ""
    res = ""
    # Iterate through the first word in strs
    for i in range(len(strs[0])):
        # Create temp str for storing chars from 1 word
        temp = strs[0][:i+1]
        # Iterate through other words in strs
        for word in strs:
            # Stop as soon as word differs from temp
            if not word.startswith(temp):
                return res
        # Update res with highest combination
        res = temp
    # Return res
    return res



# Vertical Scanning
# TC: O(N*M)     SC: O(1)
def longestCommonPrefixVS(strs: List[str]) -> str:
    # No words in strs
    if not strs:
        return ""
    # Iterate through the first word in strs
    for i in range(len(strs[0])):
        # Compare other words
        for word in strs[1:]:
            # Compare chars for words, stop when not matching
            if i >= len(word) or word[i] != strs[0][i]:
                # Return part that matched
                return strs[0][:i]
    # Complete word match
    return strs[0]



# Lexicographical Sorting Approach
# TC: O(nlogN+M)  SC: O(1)
def longestCommonPrefix(strs: List[str]) -> str:
    # Separate min and max words
    s1 = min(strs)
    s2 = max(strs)
    # Iterate through the min word
    for i in range(len(s1)):
        # Check matching words in min and max
        if s1[i] != s2[i]:
            return s1[:i]
    # Return min word if complete match
    return s1





# Custom Test Cases
q = longestCommonPrefix(["car","race","flight"])
print(q)