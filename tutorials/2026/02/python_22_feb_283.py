# Dijkstra's Shortest Path Algorithm
#=====================================

# Import the necessary libraries
import sys
import heapq

# Define a class for the Graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    # Function to print the graph
    def print_graph(self):
        for i in range(len(self.graph)):
            print(f"Vertex {i}: ", end="")
            for j in range(len(self.graph[i])):
                print(f" -> {self.graph[i][j][1]} with weight {self.graph[i][j][2]}", end=" ")
            print()

# Define a function to implement Dijkstra's algorithm
def dijkstra(graph, src):
    # Create a dictionary to store the distance to each vertex
    dist = {i: sys.maxsize for i in range(graph.V)}
    dist[src] = 0

    # Create a dictionary to store the parent of each vertex
    parent = {i: None for i in range(graph.V)}

    # Create a priority queue to store the vertices to be processed
    pq = [(0, src)]

    while pq:
        # Extract the vertex with the minimum distance from the priority queue
        (dist, u) = heapq.heappop(pq)

        # Iterate over all adjacent vertices of the extracted vertex
        for v, w in graph.graph:
            if v != u:
                # Calculate the new distance to the adjacent vertex
                new_dist = dist + w

                # If the new distance is less than the current distance, update the distance and parent
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u

                    # Add the adjacent vertex to the priority queue
                    heapq.heappush(pq, (new_dist, v))

    return dist, parent

# Main function
def main():
    # Create a graph with 5 vertices
    graph = Graph(5)

    # Add edges to the graph
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 3)
    graph.add_edge(3, 4, 2)

    # Print the graph
    graph.print_graph()

    # Apply Dijkstra's algorithm
    dist, parent = dijkstra(graph, 0)

    # Print the shortest distances and predecessors
    print("Vertex\tDistance\tPredecessor")
    for i in range(graph.V):
        print(f"{i}\t{dist[i]}\t{parent[i]}")

# Run the main function
if __name__ == "__main__":
    main()