# Breadth First Search Graph Traversal in Python

class Graph:
    def __init__(self):
        # Initialize an empty graph as a dictionary where keys are nodes and values are lists of adjacent nodes
        self.adjacency_list = {}

    def add_edge(self, node1, node2):
        # Add edge between two nodes by appending the second node to the list of adjacent nodes for the first node
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)  # For undirected graph

    def bfs(self, start_node):
        # Initialize a queue with the starting node
        visited = set()
        queue = [start_node]
        while queue:
            current_node = queue.pop(0)
            if current_node not in visited:
                print(current_node, end=" ")
                visited.add(current_node)
                # Add all adjacent nodes of the current node to the queue
                for neighbor in self.adjacency_list[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Create a sample graph
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')

# Perform BFS traversal starting from node 'A'
print("Breadth First Search Traversal:")
print()
graph.bfs('A')