# Question: Given the root of a binary tree, return the inorder traversal of its nodes' values.
# InOrder Traversal: left -> node -> right


from typing import List, Optional

# Defining a Tree Node
class TreeNode:
    # Providing default values for left, right, nodeVal
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    # Brute Force based Approach
    def inorderTraversalBF(self, root: Optional[TreeNode]) -> List[int]:
        # Store node values 
        res = []
        # Helper Func
        def dfs(node):
            # Check if node present
            if not node:
                return
            # recursively follow inOrder
            dfs(node.left)
            # Store node val into res
            res.append(node.val)
            dfs(node.right)
        # Call Helper wrt Root
        dfs(root)
        # Provide node vals
        return res
    


    # Stack based Approach
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Store node values 
        res, stack = [], []
        # Initialize Root
        curr = root
        # Check until curr/stack not empty
        while curr or stack:
            # Keep Going Left until Node
            while curr:
                # Add node to stack
                stack.append(curr)
                # Move curr to left
                curr = curr.left
            # Store stack top to curr
            curr = stack.pop()
            # Append nodeVal to res
            res.append(curr.val)
            # Check for nodes on right
            curr = curr.right
        # Provide node vals
        return res





# Custome Test Cases
q = Solution()
q1 = q.inorderTraversalBF([1,'null',2,3])
print(q1)