# Question: Given the root of a binary tree, invert the tree, and return its root.

from typing import Optional

# Defining the Tree Nodes
class TreeNode:
    # Initializing values for node, left, right
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive DFS Approach
# TC: O(N)  SC: O(N)
def invertTreeRD(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Root Not Found
    if not root:
        return None
    
    # Store Left/Right Child in tmp and Replace
    tmp = root.left
    root.left = root.right
    root.right = tmp
    # Recursively keep Switching Left/Right
    invertTreeRD(root.left)
    invertTreeRD(root.right)
    # Return Root
    return root



# Iterative Stack Approach
# TC: O(N)       SC: O(h)
def invertTreeIS(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Root not found
    if not root:
        return None
    # Defining Stack with root
    stack = [root]
    # Check till stack Empty
    while stack:
        # Pop Node one-by-one
        node = stack.pop()
        # Swap Node left, right children 
        node.left, node.right = node.right, node.left
        # Append Children to Stack
        if node.left:
            stack.append(node.left)
        # Append Children to Stack
        if node.right:
            stack.append(node.right)
    return root





# Custom Test Cases
q = invertTreeRD([4,2,7,1,3,6,9])
print(q)
