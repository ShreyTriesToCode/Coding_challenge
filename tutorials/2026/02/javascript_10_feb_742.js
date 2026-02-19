// Union Find Algorithm: Teaching you how to group elements into disjoint sets efficiently
// This algorithm is useful in solving problems involving partitioning or union of disjoint sets

class UnionFind {
  constructor(n) {
    // Initialize an array to store the parent of each element
    this.parent = Array.from({ length: n }, (_, i) => i);
    // Initialize an array to store the rank of each element
    this.rank = new Array(n).fill(0);
  }

  find(x) {
    // If x is not its own parent, find its root and set it as the parent of x
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }

  union(x, y) {
    // Find the roots of x and y
    const rootX = this.find(x);
    const rootY = this.find(y);

    // If both roots are different, merge them by making one the parent of the other
    if (rootX !== rootY) {
      if (this.rank[rootX] < this.rank[rootY]) {
        this.parent[rootX] = rootY;
      } else if (this.rank[rootX] > this.rank[rootY]) {
        this.parent[rootY] = rootX;
      } else {
        this.parent[rootY] = rootX;
        // Increment the rank of one of the roots by 1 in case they have same rank
        this.rank[rootX]++;
      }
    }
  }

  connected(x, y) {
    return this.find(x) === this.find(y);
  }
}

// Example usage:
const uf = new UnionFind(5);

uf.union(0, 1); // 0 and 1 are now in the same set
uf.union(2, 3); // 2 and 3 are now in the same set

console.log(uf.connected(0, 2)); // false, 0 and 2 are not in the same set
console.log(uf.connected(1, 2)); // true, 1 and 2 are in the same set

uf.union(4, 3); // 3 and 4 are now in the same set

console.log(uf.connected(3, 4)); // true, 3 and 4 are in the same set