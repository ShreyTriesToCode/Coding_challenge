// Heap Operations Example

// Create a min heap data structure
class MinHeap {
  constructor() {
    this.heap = [];
  }

  // Insert an element into the heap
  insert(val) {
    // Add the new value to the end of the array
    this.heap.push(val);
    // Call the heapifyUp function to maintain the heap property
    this.heapifyUp(this.heap.length - 1);
  }

  // Remove and return the smallest element from the heap
  extractMin() {
    // Check if the heap is empty
    if (this.heap.length === 0) {
      return null;
    }
    // If the heap has one element, return it
    if (this.heap.length === 1) {
      return this.heap.pop();
    }
    // Store the smallest element (root)
    let min = this.heap[0];
    // Replace the root with the last element
    this.heap[0] = this.heap.pop();
    // Call the heapifyDown function to maintain the heap property
    this.heapifyDown(0);
    return min;
  }

  // Maintain the heap property by shifting elements up
  heapifyUp(index) {
    // If the index is 0, it's the root, so nothing to do
    if (index === 0) {
      return;
    }
    // Calculate the parent index
    let parentIndex = Math.floor((index - 1) / 2);
    // If the parent is smaller than the current element, swap them
    if (this.heap[parentIndex] > this.heap[index]) {
      let temp = this.heap[parentIndex];
      this.heap[parentIndex] = this.heap[index];
      this.heap[index] = temp;
      // Recursively call heapifyUp on the parent
      this.heapifyUp(parentIndex);
    }
  }

  // Maintain the heap property by shifting elements down
  heapifyDown(index) {
    // Calculate the left and right child indices
    let leftChildIndex = 2 * index + 1;
    let rightChildIndex = 2 * index + 2;
    // Initialize the smallest index to the current index
    let smallest = index;
    // If the left child is smaller, update the smallest index
    if (leftChildIndex < this.heap.length && this.heap[leftChildIndex] < this.heap[smallest]) {
      smallest = leftChildIndex;
    }
    // If the right child is smaller, update the smallest index
    if (rightChildIndex < this.heap.length && this.heap[rightChildIndex] < this.heap[smallest]) {
      smallest = rightChildIndex;
    }
    // If the smallest index is not the current index, swap them
    if (smallest !== index) {
      let temp = this.heap[smallest];
      this.heap[smallest] = this.heap[index];
      this.heap[index] = temp;
      // Recursively call heapifyDown on the smallest index
      this.heapifyDown(smallest);
    }
  }
}

// Create a min heap
let minHeap = new MinHeap();

// Insert elements
minHeap.insert(10);
minHeap.insert(20);
minHeap.insert(5);
minHeap.insert(3);
minHeap.insert(7);

// Extract the smallest element
console.log(minHeap.extractMin()); // Output: 3
console.log(min