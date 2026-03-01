'''
#=============================================================== What is a Tree? =================================================================#
Trees are specific types of graphs. Trees are non-linear data structures that organize nodes in a hierarchy, where nodes may have children, siblings, and parent nodes.
For a graph to be classified as a tree, it must:
- Have no loops or cycles (paths where the start and end nodes are the same).
- Be connected (every node can be reached from every other node).

It consists of nodes connected by edges, forming a hierarchy from a root node at the top to leaf nodes at the bottom. 
Trees naturally represent relationships where data items have one-to-many connections, making them essential for a wide range of applications.

Core Terminologies used in Trees:
- Node: Basic unit of a tree. Contains a value and references to other nodes.
- Edge: Link between a node and its child.
- Root: Top-most node in a tree that has no parent.
- Child: A node that has a parent; direct successor of the parent.
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
- Subtree: Portion of a tree that is a tree itself.

# ===================================================== Different Types of Trees: ==================================================#
1. Binary Trees: Nodes have at-most two children [perfect, full, complete, balanced]

2. Binary Search Trees: Left subtree's node value is smaller than the root's value, and the right subtree's node value is greater than the root's value. 
                        Left and Right Subtrees must also be BSTs themselves.

3. Balanced Binary Trees: Height of the tree should be O(Log n) where n is the number of nodes. For any node, height of its left/right subtree differ by not more than 1.
    - Red-Black: Makes sure that the number of Black Nodes on every root-to-leaf path is the same and that there are no adjacent Red Nodes.
        Self Balancing BTs: they are height-balanced BSTs that automatically keep the height as small as possible when insertion and deletion operations are performed on the tree.
        - AVL: The difference between heights of left and right subtrees cannot be more than one for all nodes.
        - Red-Black: Each node has an additional attribute (red/black) to maintain balance during insertions and deletions, ensuring efficient data retrieval and manipulation.

4. Ternary Trees: Each node has atmost three child nodes (left, mid, right)

5. N-ary Trees: Generalization of BTs where each node can have atmost N child nodes.
'''

# Defining the Tree Nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





"""
#=============================================================== What is a Trie? =================================================================#
Tries are a variant of Tree data structure, used to store a set of strings.


To implement a Trie, you typically need a more specialized node than a standard TreeNode:
- Children (Dictionary/Array): Instead of left and right, each node has a collection of children (char -> node)
- isEndWord (Boolean): A flag to indicate if a node marks the completion of a valid string
- Value (Optional): Some Tries store a weight or frequency count at each node


# ===================================================== Different Types of Trie: ==================================================#
1. Standard Trie: As described above, stores every character individually.
2. Compressed Trie (Radix Tree): Merges nodes with only one child to save space. (Eg: string "internal" would be one edge instead of eight separate nodes)
3. Suffix Tree: Contains all suffixes of a given text, allowing for complex pattern matching in O(M) time where M is the pattern length.
4. Bitwise Trie: Uses bits (0 and 1) instead of characters. (Eg: often used in IP routing and networking)


Practical Uses:
- Autocomplete/Auto-suggest: Finding all words with a common prefix.
- Spell Checkers: Quickly verifying if a word exists in a dictionary.
- IP Routing: Longest prefix matching in routers to determine the next hop.
- Genome Analysis: Searching for specific DNA sequences within large datasets.
- T9 Texting: (Historical) Predicting words based on numeric keypad input.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()