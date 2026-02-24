'''
#=============================================================== What is a Graph? =================================================================#
A graph is a non-linear data structure used to represent pairwise relationships between entities. 
Formally, a graph ( G ) is denoted as ( G(V, E) ), where ( V ) is the set of vertices (nodes) and ( E ) is the set of edges (connections). 
Vertices can represent objects like people in a network or cities on a map, while edges capture the relationships or routes between these objects.


Core Terminologies used in Graphs:
- Vertex (Node): Fundamental unit representing any object or entity.
- Edge: Connection linking two vertices.
- Weight: Numeric value associated with any edge (e.g., cost, distance, or capacity).
- Degree: Number of edges connected to a vertex. (in-degree and out-degree in terms of Directed Graphs)
- Path: Sequence of edges connecting a series of vertices.
- Cycle: Path that starts and ends at the same vertex.
- Adjacent Nodes: Vertices directly connected by an edge.
- Visiting a Vertex => traversing or going to a particular vertex
- Exploring a Vertex => traversing and exploring all the adjacent vertices from a particular vertex

Different Types of Graphs:
- Undirected Graphs: Edges have no orientation. Relationships are bidirectional. Example: Facebook friendship graphs.
- Directed Graphs (Digraphs): Edges have direction. Example: Twitter follower networks or dependency modeling.
- Weighted Graphs: Edges carry a numeric value (weight). Example: Representing distances or costs in maps.
- Unweighted Graphs: All edges are treated equally.
- Connected Graphs: Graphs allow traversal from any node to any other. 
- Disconnected Graphs: Graphs have isolated components.
- Vertex Labelled Graphs: Each node is associated with a label or identifier in addition to its data. Example: transportation network (city, coordinates)
- Cyclic/Acyclic: Cyclic graphs contain cycles; acyclic graphs do not. 
=> Directed acyclic graphs (DAGs) are significant for tasks like topological sorting.

Different Ways to Represent Graphs:
- Sparse graphs (few edges relative to nodes) call for memory-efficient structures.
- Dense graphs (many edges) benefit from rapid access patterns.

#================================================================== Graph Representation in Programming? ==================================================================#
1. Adjacency List (Dynamic-sized Array / LinkedList)
An AL is an array or dictionary that stores all the neighbors of each node.
There are two ways to implement adjacency lists:
- As an array, where each index represents a node and the list stored at that index contains its neighbors.
- As a dictionary, where each key represents a node and the value associated to that key (a list) contains its neighbors.

What are the Problems?
- To check for an edge from Vertex (U) to Vertex (V), one has to traverse all neighbors. TC: O(V)

What are the Benefits?
- Saves Space: just stores info about other vertices adjacent to a particular vertex.    SC: O(V + E)
- Find Adjacents of any particular Vertex quickly.


2. Adjacency Matrix
It is a way of representing a graph as a matrix of boolean 0's and 1's. The values in the matrix represent the edges or connections between the nodes.
- The size of the matrix will be: V x V (v is the number of vertices).
- The value for mat[i][j] = 1, mat[j][i] = 1 only if there is an edge going from vertex i to vertex j or visa-versa.
- For an Undirected Graph: Matrix will always be Symmetrical. It may or may not be symmetric for directed graphs.

What are the Problems?
- Significant wastage of memory (matrix is filled with zeros).

What are the Benefits?
- Easy to check if an edge exists: Look for mat[row][col] => Operation in O(1) time.

Adjacency lists are better for sparse graphs (few edges), while adjacency matrices are efficient for dense graphs (many edges) and quick edge lookups. 

'''






'''
#=============================================================== What is a BFS? (level-order) =================================================================#
BFS traverses neighbors level by level. It visits all immediate neighbors before moving deeper. It is just like a level order on a binary tree.
It uses queue data structure for traversal. We can select any vertex as the starting vertex, and start exploring in any order. 

Rules:
- When you are selecting a vertex for exploration, you must visit all its adjacent vertices, before proceeding to next vertex for exploration!
- You should select the next vertex for exploration from the queue only!

Algorithm works like this:
- You start at a specific node.
- That node is marked as visited and added to the queue.
- While the queue is not empty, the current node is removed from the queue (dequeued). 
- Then, for each one of its neighbors, if the neighbor has not been visited, it is marked as visited and added to the queue.
=> When the queue is empty, the traversal is complete.

BFS is used for:
- Finding shortest paths in unweighted graphs (number of edges)
- Level-wise computations in trees/graphs
- Detecting connected components/cycles
- Multi-source shortest path (e.g., rotten oranges problem)

'''


'''
#=============================================================== What is a DFS? (pre-order) =================================================================#
DFS is the “diving deep” approach to graph traversal. It explores each branch as far as possible before backtracking.
It uses stack data structure for traversal. We can select any vertex as the starting point.

The algorithm works like this:
- Start at a specific node.
- That node is marked as visited and added to the stack.
- While the stack is not empty, the current node is popped (removed). This is when we "visit" or process it (for example, by printing its value). 
- Then, all of its unvisited neighbors are marked as visited and added to the stack.
=> When the stack is empty, the traversal is completed and all nodes have been visited.

Rules:
- When you visit a vertex, forget about other not visited vertices, start exploring visited vertex!
- You should store the visited vertex in stack, so that it can be explored later!

DFS is used for:
- Enumerating all nodes
- Detecting cycles
- Finding connected components
- Topological sort (in DAGs)
- Maze and puzzle solving
'''