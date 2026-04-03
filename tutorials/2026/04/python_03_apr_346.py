import collections

class Graph:
    def __init__(self):
        self.graph = {}

    # function to add an edge
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)

    # BFS Traversal of graph starting from a given vertex
    def bfs_traversal(self, start_vertex):
        visited_vertices = set()
        traversal_order = []
        queue = collections.deque()

        # add the given vertex to the queue and mark it as visited
        queue.append(start_vertex)
        visited_vertices.add(start_vertex)

        while queue:
            vertex = queue.popleft()  # remove a vertex from the front of the queue

            if vertex not in traversal_order:  # only add unvisited vertices to the order
                traversal_order.append(vertex)  # add it to the order
                print(vertex, end=' ')  # print it out for verification

            for neighbor in self.graph[vertex]:
                if neighbor not in visited_vertices:
                    queue.append(neighbor)
                    visited_vertices.add(neighbor)

# creating a graph with 5 vertices and edges
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

print("Following is the order of BFS traversal from A:")
g.bfs_traversal('A')