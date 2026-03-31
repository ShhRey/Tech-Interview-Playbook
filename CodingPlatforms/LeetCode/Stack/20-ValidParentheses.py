# Question: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
'''


# Brute Force Approach
# TC: O(N^2)       SC: O(1)
def isValid(s: str) -> bool:
        # Storing prev version of str
        prev = None
        # Keep looking until changes
        while prev != s:
            # Save curr str before modifying
            prev = s
            # Remove all valid adjacent pairs... one at a time if nested
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        # Res -> compare to blank str
        return s == ""



# Map-Stack based Approach   
# TC: O(N)  SC: O(N)
def isValid(s: str) -> bool:
    # Map close brac to open ones in a map
    hmap = { ")": "(", "]": "[", "}": "{" }
    # Initialize a stack
    stack = []
    # Iterate through every char
    for c in s:
        # If close brac found
        if c in hmap:
            # Check open brac in stack found before close
            if not stack or stack[-1] != hmap[c]:
                return False
            # If open brac present, pop stack
            stack.pop()
        # Append any other open
        else:
            # Append brac to stack
            stack.append(c)
    # Res checks if stack empty or not
    return not stack



# Stack based Approach
# TC: O(N)       SC: O(N)
def isValid(s: str) -> bool:
    # Initialize a stack
    stack = []
    # Iterate through every char
    for c in s:
        # Check for open brac
        if c == "(":
            # Add close brac in stack
            stack.append(")")
        # Check for open brac
        elif c == "{":
            # Add close brac in stack
            stack.append("}")
        # Check for open brac
        if c == "[":
            # Add close brac in stack
            stack.append("]")
        else:
            # Stack empty or diff char than brac
            if not stack or stack.pop() != c:
                return False
    # Res checks if stack empty or not
    return not stack





# Custom Test Cases
q = isValid('[]{}')
print(q)