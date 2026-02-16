# Topological Sort in Python
#=====================================================

class Graph:
    def __init__(self, vertices):
        # Initialize graph with given number of vertices
        self.V = vertices
        self.graph = []

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        # Add edge from vertex u to vertex v
        self.graph.append([u, v])

    # Function for topological sort using DFS
    def topological_sort_util(self, v, visited, stack):
        # Mark node as visited
        visited[v] = True

        # Recur for all the adjacent vertices of current node
        for i in range(len(self.graph)):
            if self.graph[i][0] == v and not visited[self.graph[i][1]]:
                self.topological_sort_util(self.graph[i][1], visited, stack)

        # Push current vertex to the stack
        stack.append(v)

    # Function for topological sort
    def topological_sort(self):
        # Initialize a list to store vertices in the order of their finish time
        visited = [False]*self.V

        # Initialize a list to store sorted vertices
        stack = []

        # Call topological_sort_util function on all vertices
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Reverse the order of vertices in stack
        stack.reverse()

        return stack

# Driver code
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Topological Sort: ")
    print(g.topological_sort())