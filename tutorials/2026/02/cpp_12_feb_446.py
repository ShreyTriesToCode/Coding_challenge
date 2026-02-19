#include <iostream>
#include <queue>
#include <vector>

// This program teaches Breadth-First Search (BFS) traversal on a graph.
// BFS is useful for traversing graphs where the order of visitation matters,
// and it's often used in network algorithms.

using namespace std;

class Graph {
    int numVertices;
    vector<vector<int>> adjList;

public:
    // Constructor to initialize the graph with given number of vertices
    Graph(int vertices) : numVertices(vertices), adjList(vertices, {}) {}

    // Function to add an edge between two vertices
    void addEdge(int src, int dest) {
        adjList[src].push_back(dest);
        adjList[dest].push_back(src);  // Assuming undirected graph
    }

    // Perform BFS traversal starting from a given source vertex
    void bfsTraversal(int src) {
        queue<int> q;  // Queue to store vertices to be visited
        vector<bool> visited(numVertices, false);  // Keep track of visited vertices

        // Mark the source vertex as visited and enqueue it
        visited[src] = true;
        q.push(src);

        while (!q.empty()) {
            int vertex = q.front();  // Dequeue a vertex to visit next
            cout << vertex << " ";

            // Enqueue all unvisited adjacent vertices of the current vertex
            for (int neighbor : adjList[vertex]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }

            q.pop();  // Remove the front element from the queue
        }
    }
};

// Example usage:
int main() {
    Graph g(5);  // Create a graph with 5 vertices

    g.addEdge(0, 1);  // Add an edge between vertex 0 and 1
    g.addEdge(0, 2);  // Add an edge between vertex 0 and 2
    g.addEdge(1, 3);  // Add an edge between vertex 1 and 3
    g.addEdge(2, 4);  // Add an edge between vertex 2 and 4

    cout << "BFS Traversal starting from vertex 0: ";
    g.bfsTraversal(0);

    return 0;
}