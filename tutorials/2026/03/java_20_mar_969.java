// Segment Tree Implementation in Java

import java.util.Scanner;

public class SegmentTree {
    // Node class representing a node in the segment tree
    static class Node {
        int minVal; // minimum value of this segment
        int maxVal; // maximum value of this segment

        public Node(int val) {
            minVal = val;
            maxVal = val;
        }

        @Override
        public String toString() {
            return "(" + minVal + ", " + maxVal + ")";
        }
    }

    // Segment Tree class
    static class SegmentTree {
        int size; // size of the segment tree
        Node[] t; // array to store nodes in the segment tree

        // Constructor to initialize the segment tree
        public SegmentTree(int[] nums) {
            size = nums.length;
            t = new Node[4 * size]; // 4 times the number of elements

            buildSegmentTree(nums, 0, size - 1, 1);
        }

        // Method to build the segment tree recursively
        private void buildSegmentTree(int[] nums, int start, int end, int index) {
            if (start == end) {
                t[index] = new Node(nums[start]);
                return;
            }

            int mid = (start + end) / 2;

            buildSegmentTree(nums, start, mid, 2 * index);
            buildSegmentTree(nums, mid + 1, end, 2 * index + 1);

            // Update the node with the minimum and maximum values
            t[index] = new Node(Math.min(t[2 * index].minVal, t[2 * index + 1].minVal),
                    Math.max(t[2 * index].maxVal, t[2 * index + 1].maxVal));
        }

        // Method to query the segment tree for range query
        public int query(int start, int end) {
            return queryHelper(0, size - 1, start, end, 1);
        }

        // Helper method for range query recursion
        private int queryHelper(int nodeStart, int nodeEnd, int queryStart, int queryEnd, int index) {
            if (nodeStart > queryEnd || nodeEnd < queryStart)
                return Integer.MAX_VALUE; // value not found

            if (queryStart <= nodeStart && nodeEnd <= queryEnd)
                return t[index];

            int mid = (nodeStart + nodeEnd) / 2;

            int leftVal = queryHelper(nodeStart, mid, queryStart, queryEnd, 2 * index);
            int rightVal = queryHelper(mid + 1, nodeEnd, queryStart, queryEnd, 2 * index + 1);

            return new Node(Math.min(leftVal.minVal, rightVal.minVal),
                    Math.max(leftVal.maxVal, rightVal.maxVal));
        }

        // Method to update the segment tree for range update
        public void update(int idx, int val) {
            updateHelper(0, size - 1, idx, val, 1);
        }

        // Helper method for range update recursion
        private void updateHelper(int nodeStart, int nodeEnd, int idx, int val, int index) {
            if (idx < nodeStart || idx > nodeEnd)
                return;

            if (nodeStart == node