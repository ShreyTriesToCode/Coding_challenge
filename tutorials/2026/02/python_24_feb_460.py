# Segment Tree Implementation in Python

## Overview

A segment tree is a data structure used for range queries and updates in an array. It is particularly useful when the array is too large to fit into memory, or when updates need to be performed on a subset of the array.

## Code

```python
class SegmentTree:
    def __init__(self, arr):
        """
        Initialize the segment tree with the given array.
        """
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 0, 0, self.n - 1)

    def build_tree(self, arr, node, start, end):
        """
        Recursively build the segment tree.
        """
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(arr, 2 * node + 1, start, mid)
            self.build_tree(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, left, right):
        """
        Query the segment tree for the sum of elements in the given range.
        """
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(2 * node + 1, start, mid, left, right) +
                self.query(2 * node + 2, mid + 1, end, left, right))

    def update(self, node, start, end, pos, val):
        """
        Update the segment tree with the given value at the specified position.
        """
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if pos <= mid:
                self.update(2 * node + 1, start, mid, pos, val)
            else:
                self.update(2 * node + 2, mid + 1, end, pos, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

# Example usage
arr = [1, 2, 3, 4, 5]
segment_tree = SegmentTree(arr)

print("Sum of elements in range (1, 3):", segment_tree.query(0, 0, segment_tree.n - 1, 1, 2))
print("Sum of elements in range (2, 4):", segment_tree.query(0, 0, segment_tree.n - 1, 2, 3))

segment_tree.update(0, 0, segment_tree.n - 1, 3, 10)
print("Sum of elements in range (1, 3) after update:", segment_tree.query(0, 0, segment_tree.n - 1, 1, 2))