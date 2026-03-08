// Segment Tree Implementation in JavaScript

// Function to calculate the minimum value in a range
function query(minValue, maxValue, left, right, tree, node) {
    // If the range is empty, return infinity
    if (left > right) {
        return Infinity;
    }
    // If the node is within the range, return the value
    if (left <= node && node <= right) {
        return tree[node];
    }
    // If the node is not within the range, find the minimum value in the child nodes
    let leftMin = Infinity;
    let rightMin = Infinity;
    if (left < node) {
        leftMin = query(minValue, maxValue, left, node - 1, tree, node * 2);
    }
    if (node < right) {
        rightMin = query(minValue, maxValue, node + 1, right, tree, node * 2 + 1);
    }
    // Return the minimum value
    return Math.min(leftMin, rightMin);
}

// Function to update the segment tree
function update(minValue, maxValue, left, right, index, value, tree) {
    // If the range is empty, do nothing
    if (left > right) {
        return;
    }
    // If the node is within the range, update the value
    if (left <= index && index <= right) {
        tree[index] = value;
    }
    // If the node is not within the range, find the child nodes and update them
    let leftChild = index * 2;
    let rightChild = index * 2 + 1;
    if (left < right) {
        if (left < leftChild) {
            update(minValue, maxValue, left, leftChild - 1, index, value, tree);
        }
        if (leftChild < right) {
            update(minValue, maxValue, leftChild + 1, right, index, value, tree);
        }
    }
}

// Function to build the segment tree
function buildSegmentTree(minValue, maxValue, left, right, tree) {
    // If the range is empty, return
    if (left > right) {
        return;
    }
    // If the node is within the range, set the value
    if (left == right) {
        tree[left] = minValue;
    } else {
        // Find the middle of the range
        let mid = Math.floor((left + right) / 2);
        // Build the left and right child nodes
        buildSegmentTree(minValue, maxValue, left, mid, tree * 2);
        buildSegmentTree(minValue, maxValue, mid + 1, right, tree * 2 + 1);
        // Set the value of the current node
        tree[left] = Math.min(query(minValue, maxValue, left, mid, tree, 1), query(minValue, maxValue, mid + 1, right, tree, 1));
    }
}

// Test the segment tree implementation
let tree = new Array(100).fill(0);
buildSegmentTree(0, 10, 0, 99, tree);
update(0, 10, 0, 99, 50, 5, tree);
console.log(query(0, 10, 0, 99, tree,