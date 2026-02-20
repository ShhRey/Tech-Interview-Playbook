"""
#======================================================= Why Advanced Graph Traversal? ====================================================#
While basic traversal algorithms like Breadth-First Search (BFS) and Depth-First Search (DFS) are essential, mastery of 
advanced graph algorithms is crucial for tackling complex problems in software engineering interviews and real-world systems.


#======================================================= Shortest Path Algorithms =========================================================#
Finding the shortest path is a central problem in graph theory, with applications in navigation, routing and scheduling.
The choice of algorithm depends on graph properties such as edge weights and cycles.

1. Dijkstra's Algorithm
It is used to find the shortest path from a single source to all other nodes in a graph with non-negative edges.
A greedy approach that always expands the node with the smallest known distance from the source. 
It uses a priority queue (min-heap) to efficiently select the next node to process.

Step by Step execution:
- Initialize distances to all nodes as infinity, except the source (distance 0).
- Use a min-heap to track nodes to visit, prioritized by current shortest distance.
- Pop the node with the smallest distance.
- For each neighbor, if the path through the current node is shorter, update the neighbor's distance and push it onto the heap.
- Repeat until all nodes are processed.

Real-World Use Cases:
- GPS and mapping: Finding the shortest driving or walking route.
- Social networks: Finding the shortest connection path between users.
- Resource allocation: Scheduling and logistics optimization.
"""

import heapq

def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances




"""
2. Bellman Ford Algorithm
It is used to find the shortest path from a single source to all other nodes in a graph, even when some edge weights are negative. 
It follows dynamic programming strategy, tries out all possible solutions and picks the best one. (Also detects negative weight cycles)
It "relaxes" all edges repeatedly, updating the shortest path estimates.

Step-by-step:
- Initialize distances to all nodes as infinity, except the source (distance 0).
- For V-1 iterations (V = number of vertices):
    - For each edge (u, v, w), if distance[u] + w < distance[v], update distance[v].
- After V-1 iterations, check all edges again. If any distance can still be updated, a negative cycle exists.

Real-World Use Cases
- Currency arbitrage detection: Negative cycles indicate arbitrage opportunities.
- Network routing: Handling networks with variable (possibly negative) costs.
- Scheduling: Detecting infeasible schedules due to negative cycles.
"""

def bellman_ford(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")
    return distances




"""
3. 
"""