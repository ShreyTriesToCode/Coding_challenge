// Union-Find Data Structure in JavaScript

class UnionFind {
    // Initialize the data structure with an array of parent pointers
    constructor(n) {
        this.parent = new Array(n);
        for (let i = 0; i < n; i++) {
            this.parent[i] = i;
        }
    }

    // Find the root of a node
    find(x) {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }

    // Check if two nodes are in the same set
    isSameSet(a, b) {
        return this.find(a) === this.find(b);
    }

    // Union two sets by making one root of the other
    union(x, y) {
        let rootX = this.find(x);
        let rootY = this.find(y);

        if (rootX !== rootY) {
            this.parent[rootX] = rootY;
        }
    }
}

// Example usage:
let n = 5;

// Create a Union-Find data structure
let uf = new UnionFind(n);

// Test cases:

console.log(uf.isSameSet(0, 1));   // Expected output: false
uf.union(0, 1);
console.log(uf.isSameSet(0, 1));   // Expected output: true

console.log(uf.isSameSet(2, 3));   // Expected output: false
uf.union(2, 3);
console.log(uf.isSameSet(2, 3));   // Expected output: true

console.log(uf.parent[0]);       // Expected output: 0
console.log(uf.parent[1]);       // Expected output: 0
console.log(uf.parent[2]);       // Expected output: 2
console.log(uf.parent[3]);       // Expected output: 2

// Run the example:
let n = 5;
uf = new UnionFind(n);
uf.union(0, 1);
uf.union(2, 3);
uf.union(4, 5);

console.log(uf.isSameSet(0, 4));   // Expected output: true
console.log(uf.isSameSet(1, 4));   // Expected output: false
console.log(uf.isSameSet(0, 5));   // Expected output: true