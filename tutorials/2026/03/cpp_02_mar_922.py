#include <iostream>

class UnionFind {
public:
    UnionFind(int n) : n(n), parent(n) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }

    bool connected(int x, int y) {
        return find(x) == find(y);
    }

private:
    int n;
    int* parent;
};

int main() {
    UnionFind uf(6);
    uf.unionSets(0, 1);
    uf.unionSets(1, 2);
    uf.unionSets(3, 4);
    uf.unionSets(5, 0);
    std::cout << std::boolalpha << uf.connected(0, 1) << std::endl;  // Output: true
    std::cout << std::boolalpha << uf.connected(1, 2) << std::endl;  // Output: true
    std::cout << std::boolalpha << uf.connected(3, 4) << std::endl;  // Output: true
    std::cout << std::boolalpha << uf.connected(5, 0) << std::endl;  // Output: true
    std::cout << std::boolalpha << uf.connected(3, 5) << std::endl;  // Output: false
    return 0;
}