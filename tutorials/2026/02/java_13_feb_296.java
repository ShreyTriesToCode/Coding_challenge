public class UnionFind {
    private int[] parent;
    private int[] rank;

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }

    // Finds the root of a node
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Union two sets
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY)
            return;

        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }

    public static void main(String[] args) {
        UnionFind uf = new UnionFind(10);

        // Test case 1:
        //   - Set {0, 1, 2}
        //   - Union {3, 4, 5} with above set
        //   - Expected output: [{0, 1, 2, 3}, {4, 5}]
        uf.union(0, 1);
        uf.union(1, 2);
        uf.union(3, 4);
        uf.union(4, 5);

        System.out.println("Parent of 0: " + uf.find(0));
        System.out.println("Parent of 1: " + uf.find(1));
        System.out.println("Parent of 2: " + uf.find(2));
        System.out.println("Parent of 3: " + uf.find(3));
        System.out.println("Parent of 4: " + uf.find(4));
        System.out.println("Parent of 5: " + uf.find(5));

        // Test case 2:
        //   - Set {0, 1}
        //   - Union {2, 3, 4} with above set
        //   - Expected output: [{0, 1, 2, 3}, {4}]
        uf.union(0, 1);
        uf.union(5, 6);
        uf.union(7, 8);
        uf.union(9, 10);

        System.out.println("Parent of 0: " + uf.find(0));
        System.out.println("Parent of 1: " + uf.find(1));
        System.out.println("Parent of 2: " + uf.find(2));
        System.out.println("Parent of 3: " + uf.find(3));
        System.out.println("Parent of 4: " + uf.find(4));
    }
}