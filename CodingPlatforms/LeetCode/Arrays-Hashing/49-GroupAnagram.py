# Question: Given an array of strings strs, group the anagrams together. You can return the answer in any order

from typing import List
from collections import defaultdict

# Brute Force Approach
# TC: O(N^2 * klogk)        SC: O(N)

# Acting as Helper Func
def isAnagram(s, t):
    return sorted(s) == sorted(t)
def groupAnagramsBF(strs: List[str]) -> List[List[str]]:
    # Taking note of str checked + grouped
    visited = [False] * len(strs)
    # Grouping strs for result
    res = []
    # Traverse List of strs and pick 1
    for i in range(len(strs)):
        # If already in visited
        if visited[i]:
            continue
        # Start new group
        group = [strs[i]]
        # mark str visited
        visited[i] = True
        # Check with other strs 
        for j in range(i+1, len(strs)):
            # Possible anagram: not in visited and helper func
            if not visited[j] and isAnagram(strs[i], strs[j]):
                # Add sec str in group
                group.append(strs[j])
                # Mark sec-str in visited
                visited[j] = True
        # Add group in result
        res.append(group)
    return res



# Sorting-based Approach
# TC: O(N *Klog(K))    SC: O(N*K)
def groupAnagramsS(strs: List[str]) -> List[List[str]]:
    # Creating def-dict with list
    group = defaultdict(list)
    # Iterating through every str
    for s in strs:
        # Prep key for dict, matching char
        key = ''.join(sorted(s))
        # Grouping with same chars
        group[key].append(s)
    # List in desired format
    return list(group.values())



# ASCII-based Approach
# TC: O(N*K)    SC: O(N*K)
def groupAnagramsASC(strs: List[str]) -> List[List[str]]:
    # Creating def-dict with list
    group = defaultdict(list)
    # Iterating every str in list
    for s in strs:
        # Standard char arr
        count = [0] * 26
        for c in s:
            # Map Characters and Update Count
            count[ord(c) - ord('a')] += 1
            # Tuple to be used as key for dict
        key = tuple(count)
        # Group as per matching key
        group[key].append(s)
    # List in desired format
    return list(group.values())





# Custom Test Cases
q = groupAnagramsASC(["eat","tea","tan","ate","nat"])
print(q)