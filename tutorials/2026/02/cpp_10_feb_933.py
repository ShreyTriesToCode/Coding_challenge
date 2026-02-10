#include <iostream>
#include <vector>

class UnionFind {
public:
    // Initialize the parent array to store the root of each set
    UnionFind(int n) : parent(n + 1), rank(n + 1) {
        for (int i = 0; i <= n; ++i)
            parent[i] = i;
    }

    // Find the root of a node
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    // Check if two nodes are in the same set
    bool union_(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY)
            return false;

        if (rank[rootX] < rank[rootY])
            parent[rootX] = rootY;
        else if (rank[rootX] > rank[rootY])
            parent[rootY] = rootX;
        else {
            parent[rootY] = rootX;
            ++rank[rootX];
        }
        return true;
    }

private:
    std::vector<int> parent, rank;
};

int main() {
    // Example usage
    UnionFind uf(5);

    // Initially, each node is in its own set
    std::cout << "Initially:" << std::endl;
    for (int i = 1; i <= 5; ++i) {
        std::cout << i << " -> " << uf.find(i) << std::endl;
    }

    // Merge sets
    uf.union_(2, 3);
    uf.union_(4, 5);

    // Check if nodes are in the same set
    std::cout << "\nAfter merging sets:" << std::endl;
    std::cout << "2 -> " << uf.find(2) << ", 3 -> " << uf.find(3) << std::endl;  // Should print 0
    std::cout << "4 -> " << uf.find(4) << ", 5 -> " << uf.find(5) << std::endl;  // Should print 0

    // Merging two sets with the same size is equivalent to not merging them at all
    uf.union_(1, 6);

    return 0;
}