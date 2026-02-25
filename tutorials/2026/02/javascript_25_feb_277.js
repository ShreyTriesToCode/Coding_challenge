// graph_traversal.js
// Breadth-First Search (BFS) Traversal of a Graph

class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  // Add a node to the graph
  addNode(node) {
    this.adjacencyList[node] = [];
  }

  // Add an edge between two nodes
  addEdge(node1, node2) {
    if (!this.adjacencyList[node1]) this.addNode(node1);
    if (!this.adjacencyList[node2]) this.addNode(node2);
    this.adjacencyList[node1].push(node2);
    this.adjacencyList[node2].push(node1);
  }

  // Perform BFS traversal of the graph
  bfsTraversal(startNode) {
    const visited = new Set();
    const queue = [startNode];

    while (queue.length > 0) {
      const node = queue.shift();
      console.log(node);

      for (const neighbor of this.adjacencyList[node]) {
        if (!visited.has(neighbor)) {
          visited.add(neighbor);
          queue.push(neighbor);
        }
      }
    }
  }
}

// Example usage
const graph = new Graph();
graph.addNode('A');
graph.addNode('B');
graph.addNode('C');
graph.addNode('D');
graph.addEdge('A', 'B');
graph.addEdge('A', 'C');
graph.addEdge('B', 'D');
graph.addEdge('C', 'D');

graph.bfsTraversal('A');