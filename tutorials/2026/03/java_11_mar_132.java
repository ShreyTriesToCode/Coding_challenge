// Segment Tree Java Implementation

public class SegmentTree {

    // Node class representing a segment of the segment tree
    static class Node {
        int min, max;
        Node left, right;

        // Constructor for a new Node
        public Node(int min, int max) {
            this.min = min;
            this.max = max;
        }
    }

    // Segment Tree class
    public static class SegmentTree {
        // Array to store nodes of the segment tree
        private Node[] tree;
        // Size of the array representing the segment tree
        private int size;

        // Constructor for a new SegmentTree
        public SegmentTree(int[] arr) {
            // Calculate the size of the segment tree
            size = arr.length;
            // Initialize the tree with null nodes
            tree = new Node[size * 4];
            // Build the segment tree
            buildTree(0, 0, size - 1, arr);
        }

        // Function to build the segment tree
        private void buildTree(int node, int start, int end, int[] arr) {
            // Base case: if the start index is equal to the end index
            if (start == end) {
                // Create a new node with the minimum and maximum values
                tree[node] = new Node(arr[start], arr[start]);
            } else {
                // Calculate the middle index
                int mid = (start + end) / 2;
                // Recursively build the left and right subtrees
                buildTree(node * 2 + 1, start, mid, arr);
                buildTree(node * 2 + 2, mid + 1, end, arr);
                // Create a new node with the minimum and maximum values of the left and right subtrees
                tree[node] = new Node(Math.min(tree[node * 2 + 1].min, tree[node * 2 + 2].min),
                        Math.max(tree[node * 2 + 1].max, tree[node * 2 + 2].max));
            }
        }

        // Function to query the segment tree
        public int query(int node, int start, int end, int l, int r) {
            // Base case: if the query range is empty
            if (start > end || l > r) {
                return Integer.MAX_VALUE;
            }
            // Base case: if the query range is within the current node
            if (l <= start && r >= end) {
                return tree[node].min;
            }
            // Calculate the middle index
            int mid = (start + end) / 2;
            // Recursively query the left and right subtrees
            return Math.min(query(node * 2 + 1, start, mid, l, r), query(node * 2 + 2, mid + 1, end, l, r));
        }

        // Function to update the segment tree
        public void update(int node, int start, int end, int index, int value) {
            // Base case: if the start index is equal to the end index
            if (start == end) {
                // Update the node with the new value
                tree[node] = new Node(value, value);
            } else {
                // Calculate the middle index
                int mid = (start + end) /