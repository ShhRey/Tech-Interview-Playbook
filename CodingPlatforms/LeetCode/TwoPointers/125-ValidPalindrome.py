# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#  Question: Given a string s, return true if it is a palindrome, or false otherwise.

# Brute Force Approach   
# TC: O(N)  SC: O(N)
def isPalindromeBF(s: str) -> bool:
    # Initialize blank string/list -> ""/[]
    res = ""
    # Iterate through input str
    for char in s:
        # Only add if char isalnum()
        if char.isalnum():
            # Append char to res
            # res.append(char.lower())
            res += char.lower()
    # Compare with reverse and return res
    return res == res[::-1]



# 2Ptr Approach   
# TC: O(N)  SC: O(1)
def isPalindrome(s: str) -> bool:
    # If input str empty
    if len(s) == 0:
        return True
    # Make sure input str uni-case
    s = s.lower()
    # Create left and right pointers
    l, r = 0, len(s)-1
    # Keep checking until left < right
    while l < r:
        # Ignore non-alnum chars from left
        while l < r and not s[l].isalnum():
            l += 1
        # Ignore non-alnum chars from right
        while l < r and not s[r].isalnum():
            r -= 1
        # Compare left and right
        if s[l] != s[r]:
            return False
        # Update left/right ptrs
        l += 1
        r -= 1
    # Return True
    return True
        




# Custom Test Cases
q = isPalindrome('racecar')
print(q)