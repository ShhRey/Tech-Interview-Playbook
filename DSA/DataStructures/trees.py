'''
#=============================================================== What is a Tree? =================================================================#
A tree is a non-linear data structure used to represent data in a parent-child relationship.
It consists of nodes connected by edges, forming a hierarchy from a root node at the top to leaf nodes at the bottom. 
Trees naturally represent relationships where data items have one-to-many connections, making them essential for a wide range of applications.

Core Terminologies used in Trees:
- Node: Basic unit of a tree. Contains a value and references to other nodes.
- Edge: Link between a node and its child.
- Root: Top-most node in a tree that has no parent.
- Leaf: Node that has no children, usually at bottom of tree.
- Parent: Node that has children, direct predecessor for child nodes.
- Internal: Any node that has atleast one child.
- Siblings: Nodes that share the same parent.
- Ancestor: Any node that can be reached by repeatedly traversing parent references (upstream from given).
- Descendent: Any node that can be reached by repeatedly traversing child references (downstream from given).
- Level/Depth: The distance / number of edges from root to given node. [Root will always be Lvl 0]
- Degree: Number of children from a node.
- Height: Length of the longest path from a node to leaf.
- Diameter: Number of edges in the longest path between any two nodes.

# ===================================================== Different Types of Trees: ==================================================#
1. Binary Trees: Nodes have at-most two children [perfect, full, complete, balanced]

2. Binary Search Trees: Left child's value is smaller than the parent's value, and the right child's value is greater.
    Properties:
        => All values in the left sub-tree for a node should also have values less than the node.
        => All values in the right sub-tree for a node should also have values greater than or equal to the node.

3. Balanced Binary Trees:  [AVL, Red-Black, B-Tree]

4. Ternary Trees: Each node has atmost three child nodes (left, mid, right)

5. N-ary Trees: Generalization of BTs where each node can have atmost N child nodes.



#================================================================== Tree Representation in Programming? ==================================================================#
1. Adjacency List
It represents nodes as keys of dictionary, where each value is a list of neighboring nodes, typically children.
This format is efficient for sparse trees since nodes without children require little storage.

What are the Problems?
- 

What are the Benefits?
- Space-efficient for trees with many leaves.
- Naturally fit for representing hierarchies (such as: organizational charts).



2. Adjacency Matrix
It is a way of representing a tree as a matrix of boolean 0's and 1's. 
An adjacency matrix is a 2D list (or array) where entry [i][j] is 1 if there is an edge from node i to node j, and 0 otherwise

What are the Problems?
- Stores redundant information.

What are the Benefits?
- Easy to check if an edge exists => Operation in O(1) time.
'''


# Defining the Tree Nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right