#include <iostream>
#include <vector>

// Union-Find data structure
class UnionFind {
private:
    std::vector<int> parent;
    std::vector<int> rank;

    // Function to find the parent of a node
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Function to union two nodes
    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }

public:
    // Constructor
    UnionFind(int size) {
        parent.resize(size);
        rank.resize(size, 0);

        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
    }

    // Function to check if two nodes are connected
    bool isConnected(int x, int y) {
        return find(x) == find(y);
    }

    // Function to union two nodes
    void unionNodes(int x, int y) {
        unionSet(x, y);
    }
};

int main() {
    // Create a Union-Find data structure with 5 nodes
    UnionFind uf(5);

    // Test cases
    std::cout << "Test case 1: " << (uf.isConnected(0, 1) ? "Yes" : "No") << std::endl; // Output: No
    std::cout << "Test case 2: " << (uf.isConnected(0, 4) ? "Yes" : "No") << std::endl; // Output: No
    std::cout << "Test case 3: " << (uf.isConnected(0, 1) ? "Yes" : "No") << std::endl; // Output: Yes
    uf.unionNodes(0, 1);
    std::cout << "Test case 4: " << (uf.isConnected(0, 1) ? "Yes" : "No") << std::endl; // Output: Yes

    return 0;
}