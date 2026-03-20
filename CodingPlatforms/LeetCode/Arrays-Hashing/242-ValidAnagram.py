# Question: Given two strings s and t, return true if t is an anagram of s, and false otherwise

from collections import Counter


# Sorting based Approach
# TC: O(nlogn)      SC: O(N)
def isAnagramS(s: str, t: str) -> bool:
    # Sort both strings and compare
    return sorted(s) == sorted(t)



# 2 HashMap-based Approach
# TC: O(N)      SC: O(N)
def isAnagram2M(s: str, t: str) -> bool:
    # Stop if len different
    if len(s) != len(t):
        return False
    # Create a hmap for both strings
    smap, tmap = {}, {}
    # Map characters with count for each
    for c in s:
        smap[c] = smap.get(c, 0) + 1
    # Map characters with count for each
    for c in t:
        tmap[c] = tmap.get(c, 0) + 1
    # Compare both maps
    return smap == tmap



# 1 HashMap-based Approach
# TC: O(N)      SC: O(N)
def isAnagram1M(s: str, t: str) -> bool:
    # Stop if len different
    if len(s) != len(t):
        return False
    # 1 map for any string
    cmap = {}
    # Map characters incrementing count
    for c in s:
        cmap[c] = cmap.get(c, 0) + 1
    # Check char same map, decrement count
    for c in t:
        if c not in cmap or cmap[c] == 0:
            return False
        # Decrement
        cmap[c] -= 1
    # If empty, Match
    return True



# Counter-based Approach
# TC: O(N)    SC: O(N)
def isAnagramC(s: str, t: str) -> bool:
    # One Liner Solution
    return Counter(s) == Counter(t)



# Fix-Array based Solution
# TC: O(N)      SC: O(1)
def isAnagramA(s: str, t: str) -> bool:
    # Stop if len different
    if len(s) != len(t):
        return False
    # Every char Array
    count = [0] * 26
    for i in range(len(s)):
        # Inc char count from s
        count[ord(s[i]) - ord('a')] += 1
        # Dec char count from t
        count[ord(t[i]) - ord('a')] -= 1
    # True if all char count is 0
    return all(c == 0 for c in count)       





# Custom Test Cases
q = isAnagram1M("car", "car")
print(q)