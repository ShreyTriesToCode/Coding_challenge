// Heap Operations in JavaScript
// By [Your Name]

class MinHeap {
    constructor() {
        // Initialize an empty array to store the elements of the heap.
        this.heap = [];
    }

    insert(value) {
        // Add a new element to the end of the heap.
        this.heap.push(value);
        
        // Call the siftUp method to maintain the heap property.
        this.siftUp(this.heap.length - 1);
    }

    extractMin() {
        // If the heap is empty, return null.
        if (this.heap.length === 0) {
            return null;
        }
        
        // If the heap has only one element, remove and return it.
        if (this.heap.length === 1) {
            return this.heap.pop();
        }

        // Store the minimum value at the root of the heap.
        let min = this.heap[0];
        
        // Replace the root with the last element in the heap.
        this.heap[0] = this.heap.pop();

        // Call the siftDown method to maintain the heap property.
        this.siftDown(0);

        return min;
    }

    siftUp(index) {
        // If the index is 0, it means we are at the root of the heap. 
        // So, we don't need to do anything.
        if (index === 0) {
            return;
        }
        
        // Calculate the parent index.
        let parentIndex = Math.floor((index - 1) / 2);

        // If the element at the current index is less than its parent, 
        // swap them and continue the process until we reach the root.
        if (this.heap[index] < this.heap[parentIndex]) {
            [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
            this.siftUp(parentIndex);
        }
    }

    siftDown(index) {
        // Calculate the left and right child indices.
        let leftChildIndex = 2 * index + 1;
        let rightChildIndex = 2 * index + 2;

        // Initialize the smallest index to the current index.
        let smallest = index;

        // Check if the left child is smaller than the current element. 
        // If so, update the smallest index and swap them if necessary.
        if (leftChildIndex < this.heap.length && this.heap[leftChildIndex] < this.heap[smallest]) {
            smallest = leftChildIndex;
        }

        // Check if the right child is smaller than the current element. 
        // If so, update the smallest index and swap them if necessary.
        if (rightChildIndex < this.heap.length && this.heap[rightChildIndex] < this.heap[smallest]) {
            smallest = rightChildIndex;
        }

        // If the smallest index is not the current index, swap them and continue the process until we reach the root.
        if (smallest !== index) {
            [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
            this.siftDown(smallest);
        }
    }

    // Example usage:
    heapExample() {
        let minHeap = new MinHeap();

        minHeap.insert(10);
        minHeap.insert(20);
        minHeap.insert(5);
        minHeap.insert(15);

        console.log(minHeap.extractMin());  // Output: