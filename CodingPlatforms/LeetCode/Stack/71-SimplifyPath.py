# Question: You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
# Your task is to transform this absolute path into its simplified canonical path. The rules of a Unix-style file system are as follows:
"""
- Single period '.' represents the current directory
- Double period '..' represents the previous/parent directory
- Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'
- Any sequence of periods that does not match the rules above should be treated as a valid directory or file name
"""

# Iterate Stack Approach
# TC: O(N)       SC: O(N)
def simplifyPath2(path: str) -> str:
    stack = []
    curr = ""
    # Iterate through the path
    for c in path:
        # Cond on curr str
        if c =="/":
            # parent directory
            if curr == "..":
                # Check for stack
                if stack:
                    # pop last part
                    stack.pop()
            # add new directories and upd stack
            elif curr != "" or curr != ".":
                stack.append(curr)
            # empty curr
            curr = ""
        # Append curr str
        else:
            # add next char
            curr += c
    return "/" + "/".join(stack)



# Split Stack Approach
# TC: O(N)       SC: O(N)
def simplifyPath1(path: str) -> str:
    # Initialize Stack
    stack = []
    # Split path wrt /
    for part in path.split("/"):
        # Case1: current directory
        if part == "" or part == ".":
            # Ignore and move forward
            continue
        # Case2: parent directory
        elif part == "..":
            # Only pop if stack
            if stack: 
                stack.pop()
        # Case3: add child directory
        else:
            # Append into stack
            stack.append(part)
    # Format back single path as string
    return "/" + "/".join(stack)





# Custom Test Cases
q = simplifyPath1("home/./abc/def/../api")
print(q)