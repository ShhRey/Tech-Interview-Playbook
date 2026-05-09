# Question: Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from typing import Optional

# Defining the Tree Nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def maxDepthRD(root: Optional[TreeNode]) -> int:
    # Exit if not Nodes
    if not root:
        return 0
    # Recursively check maxD for left and right child, Add 1 for root
    return 1 + max(maxDepthRD(root.left), maxDepthRD(root.right))



# Stack based Approach
# TC: O(N)  SC: O(h)
def maxDepthSD(root: Optional[TreeNode]) -> int:
    # Exit if no Nodes
    if not root:
        return 0
    # If Root, default Depth = 1
    res = 0
    stack = [[root, 1]]
    # Check until stack Empty
    while stack:
        # Segregate Node and Depth Val
        node, depth = stack.pop()
        # This will Ignore Null
        if node:
            # Check maxD, compare res
            res = max(res, depth)
            # If child, increment depth by 1
            stack.append(root.left, depth+1)
            stack.append(root.right, depth+1)
    # Return maxD
    return res


# Custom Test Cases
q = maxDepthRD([3,9,20,'null','null',15,7])
print(q)