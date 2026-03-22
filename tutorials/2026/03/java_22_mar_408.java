import java.util.*;

public class TopologicalSort {
    // Step 1: Define the Graph class to represent a directed graph
    static class Graph {
        int V; // Number of vertices in the graph
        List<List<Integer>> adj;

        public Graph(int vertices) {
            V = vertices;
            adj = new ArrayList<>();
            for (int i = 0; i < V; i++) {
                adj.add(new ArrayList<>());
            }
        }

        // Step 2: Add an edge to the graph
        void addEdge(int u, int v) {
            adj.get(u).add(v);
        }

        // Step 3: Perform topological sort using DFS and visited arrays
        List<Integer> topologicalSort() {
            boolean[] visited = new boolean[V];
            List<Integer> order = new ArrayList<>();
            for (int i = 0; i < V; i++) {
                if (!visited[i]) {
                    dfs(i, visited, order);
                }
            }
            return order;
        }

        // Step 4: Perform DFS traversal to check for cycles and build the ordering
        void dfs(int v, boolean[] visited, List<Integer> order) {
            visited[v] = true;

            // Visit all adjacent vertices first
            for (int i : adj.get(v)) {
                if (!visited[i]) {
                    dfs(i, visited, order);
                }
            }

            // Add current vertex to the ordering after visiting all its neighbors
            order.add(v);
        }
    }

    public static void main(String[] args) {
        // Create a sample graph with 5 vertices and 8 edges
        Graph g = new Graph(5);
        g.addEdge(1, 0);
        g.addEdge(2, 0);
        g.addEdge(3, 4);
        g.addEdge(3, 2);
        g.addEdge(4, 1);

        // Perform topological sort on the graph
        List<Integer> order = g.topologicalSort();
        System.out.println("Topological Order: " + order);

        // Print the final ordering of vertices
        for (int i : order) {
            System.out.print(i + " ");
        }
    }
}