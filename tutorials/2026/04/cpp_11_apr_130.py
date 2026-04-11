#include <iostream>
#include <vector>

using namespace std;

// Function to calculate the sum of an interval in the array
int get_sum(int* seg_tree, int start, int end, int node, int s, int e) {
    // If the current node's range does not overlap with the given interval, return 0
    if (end < node || start > e)
        return 0;
    // If the current node overlaps with the entire array, return the sum of all elements in the tree
    if (start >= s && end <= e) {
        return seg_tree[node];
    }
    // Recursively calculate the sum for the left and right child nodes
    int mid = (s + e) / 2;
    return get_sum(seg_tree, start, end, node*2, s, mid) +
           get_sum(seg_tree, start, end, node*2+1, mid+1, e);
}

// Function to update the sum in a segment tree
void update(int* seg_tree, int node, int start, int end, int idx, int val) {
    // If the current node's range does not overlap with the given index, return
    if (end < idx || start > idx)
        return;
    // If the current node is a leaf node and its value needs to be updated
    if (start == end) {
        seg_tree[node] = val;
        return;
    }
    int mid = (start + end) / 2;
    update(seg_tree, node*2, start, mid, idx, val);
    update(seg_tree, node*2+1, mid+1, end, idx, val);
    // Update the sum of the current node with the sums from its child nodes
    seg_tree[node] = seg_tree[node*2] + seg_tree[node*2+1];
}

int main() {
    int n;
    cin >> n;

    // Create an array to store input values
    int arr[n];

    for (int i = 0; i < n; i++)
        cin >> arr[i];

    // Initialize the segment tree with zeros
    vector<int> seg_tree(4*n);
    fill(seg_tree.begin(), seg_tree.end(), 0);

    // Build the segment tree
    for (int i = 0; i < n; i++) {
        update(&seg_tree[1], 1, 0, n-1, i, arr[i]);
    }

    // Calculate the sum of an interval in the array
    int start, end;
    cin >> start >> end;
    cout << get_sum(&seg_tree[1], start, end, 1, 0, n-1) << endl;

    return 0;
}