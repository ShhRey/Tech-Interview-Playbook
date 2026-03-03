"""
#=============================================================== What is a Priority Queue? =================================================================#
Priority queue is an abstract data type (ADT) that works similarly to a queue or stack, but with one key difference. 
It takes the 'priority' of the elements into account. The priority is used to determine which element should be removed next.
Usually, the element with the highest priority is removed first, but some implementations may also choose to remove the element with the lowest priority first.

Practical Uses:
- Finding the shortest path between two locations
- Scheduling tasks in operating systems
- Simulating traffic, compressing data, and managing networks

In Python, priority queues are implemented using a heap data structure.





#=============================================================== What is a Heap? =================================================================#
Heap is a tree data structure with a very specific propery; this property determines the relationship between each node and its children, based on heap type.
Heaps are typically implemented as arrays to access parent and child nodes effectively.
In Python, heapq is a built-in module that one can use to work with a default implementation of min-heap.

Using arrays simplifies the logic for accessing these values or nodes; if heap maintains the structure of a complete binary tree. 
It only requires small mathematical operations based on their indices to find where the elements are located in the memory:

For a node at index i:
- Parent index: (i - 1) // 2
- Left child index: 2 * i + 1
- Right child index: 2 * i + 2

There are two primary types of heap:
=> Min Heap: the value of each node is smaller than or equal to the value of its children
=> Max Heap: the value of each node is greater than or equal to the value of its children


By default, heapq sorts elements by their natural order (smallest value first). To use custom priorities, store elements as tuples (priority, element).

If two elements have the same priority and insertion order matters, use:    (priority, counter, element)
This ensures elements with equal priority are removed in the order they were inserted.



#=============================================================== Why Heaps and Priority Queues Matter =================================================================#
Heaps allow efficient retrieval of the most important (highest or lowest priority) element.
Because insertion and removal are logarithmic time, they are highly efficient for large datasets.

This efficiency is crucial for:
- Dijkstra algorithm (shortest path)
- Task scheduling systems
- Event-driven simulations
- Network routing



#=========================================================== Working with heapq in Python ======================================================#
To use heapq module:   import heapq

1) Create an empty heap:
    my_heap = []

2) Insert elements:
    heapq.heappush(my_heap, element)
   Time Complexity: O(log n)

3) Remove and return the smallest element:
    heapq.heappop(my_heap)
   Time Complexity: O(log n)

4) Push then pop in one operation:
    heapq.heappushpop(my_heap, element)
   More efficient than separate push and pop.
   Time Complexity: O(log n)

5) Convert an existing list into a heap:
    heapq.heapify(my_heap)
   Time Complexity: O(n)
"""