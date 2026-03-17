// Topological Sort in JavaScript

class Graph {
    constructor() {
        // Initialize an empty graph object
        this.graph = {};
    }

    // Add a node to the graph
    addNode(node) {
        // If the node doesn't exist, create it and set its neighbors as an empty array
        if (!this.graph[node]) {
            this.graph[node] = [];
        }
    }

    // Add an edge between two nodes
    addEdge(from, to) {
        // Check if both nodes exist in the graph
        if (from in this.graph && to in this.graph) {
            // Add the node 'to' as a neighbor of node 'from'
            this.graph[from].push(to);
        }
    }

    // Perform topological sort using DFS
    topologicalSort() {
        // Initialize an array to store the sorted nodes
        let visited = new Array(Object.keys(this.graph)).fill(false);

        // Initialize an array to store the sorted order
        let order = [];

        // Define a helper function for DFS
        function dfs(node) {
            // Mark the current node as visited
            visited[node] = true;

            // Recur for all neighbors of the current node
            for (let neighbor of this.graph[node]) {
                if (!visited[neighbor]) {
                    dfs(neighbor);
                }
            }

            // Push the current node to the sorted order array
            order.push(node);
        }

        // Perform DFS traversal on all unvisited nodes
        for (let node in this.graph) {
            if (!visited[node]) {
                dfs(node);
            }
        }

        // Return the sorted order of nodes
        return order.reverse();
    }
}

// Create a new graph object
let g = new Graph();

// Add nodes to the graph
g.addNode('A');
g.addNode('B');
g.addNode('C');
g.addNode('D');

// Add edges between nodes
g.addEdge('A', 'B');
g.addEdge('A', 'C');
g.addEdge('B', 'D');
g.addEdge('C', 'D');

// Perform topological sort
let sortedOrder = g.topologicalSort();

// Print the sorted order of nodes
console.log("Topological Sort:");
for (let node of sortedOrder) {
    console.log(node);
}