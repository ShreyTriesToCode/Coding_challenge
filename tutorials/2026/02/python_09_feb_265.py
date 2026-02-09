# Topological Sort in Python

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # default graph
        self.graph = [[] for i in range(vertices)]

    # function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # function to check if a vertex is visited or not
    def is_visited(self, v):
        return True if len(self.visited[v]) > 0 else False

    # function to perform DFS on the graph
    def dfs_util(self, v):
        self.visited[v] = [v]
        for i in self.graph[v]:
            if self.is_visited(i) == False:
                self.dfs_util(i)
                self.visited[v].extend(self.visited[i])
        return sorted(self.visited[v])

    # function to perform topological sort
    def topological_sort(self):
        # create a list to store visited vertices
        self.visited = [False] * (self.V)

        for i in range(0, self.V):
            if self.is_visited(i) == False:
                self.dfs_util(i)
        return self.visited

# function to test the topological sort algorithm
def test_topological_sort(graph):
    print("Topological Sort: ", graph.topological_sort())

# create a directed acyclic graph with 6 vertices and 5 edges
g = Graph(6)

g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

test_topological_sort(g)