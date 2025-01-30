#bfs_graph_traversal

from collections import deque


def bfs(graph, start):
    visited = set()  # Step 1: Initialize an empty set to track visited nodes.
    queue = deque([start])  # Step 2: Initialize a queue with the starting node.
    
    while queue:  # Step 3: Loop while there are elements in the queue.
        vertex = queue.popleft()  # Step 4: Dequeue a node from the front of the queue.
        if vertex not in visited:  # Step 5: Check if the node has already been visited.
            visited.add(vertex)  # Step 6: Mark the node as visited.
            queue.extend(set(graph[vertex]) - visited)  # Step 7: Add unvisited neighbors to the queue.
    
    return visited  # Step 8: Return the set of visited nodes.

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs(graph, 'A'))  # Expected output: {'A', 'B', 'C', 'D', 'E', 'F'}