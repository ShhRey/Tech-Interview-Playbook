'''
#=============================================================== What is a Linked List? =================================================================#
A linked list is a dynamic linear data structure composed of individual elements called nodes.
Each node contains two components:  1. data (payload)    2. reference (pointer) to the next node
They differ fundamentally from an array, where elements are stored in sequential memory blocks, with pre-allocated sizes.

Core Terminologies used in Linked Lists:
- Node: Elementary unit of a LL that holds actual data and one or more references.
- Head: The first node in the LL. Entry point for all traversal and operations.
- Tail: The last node in non-circular LLs whose next reference is typically None.
- Dummy: Used to simplify logic for insertions and deletions at list boundaries.
- Traversal: Process of sequentially visiting each node, starting from the Head.
=> Nodes can be scattered anywhere in memory, supporting dynamic sizing and allocation.


Different Types of LLs:
- Singly LL (Forward Traversal): Each node has single reference pointing to the next node.                  Example: Stacks, Sequences
- Doubly LL (Bi-directional): Each node contains two references, pointing to both next and prev nodes.      Example: Undo-stack, Playlists
- Circular LL (Cyclic): Last node's next reference points back to the head, forming a loop.                 Example: Scheduling, Buffering Sys
=> Circular SLL / DLL: Continuous Looping / Bi-directional Looping
'''

#  Representing a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#====================== Figuring out how SLL Operates ======================#
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Prepend: Directly adjusts the head, constant-time operation.
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Append: Requires traversal unless a tail pointer is maintained.
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # After a Specified Node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Given node is None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Deleting a Node wrt value
    def delete_by_value(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return  # Not found
        if prev is None:
            self.head = current.next  # Remove head
        else:
            prev.next = current.next

    # Searching for Element in LL
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False


    # Traversing a Linked List: O(N)
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


