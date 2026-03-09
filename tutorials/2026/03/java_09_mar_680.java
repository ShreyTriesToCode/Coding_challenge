// Heap Operations in Java

import java.util.*;

public class HeapOperations {

    // Heap class implementation
    static class Heap {
        int[] heap;
        int size;

        // Constructor to initialize the heap
        public Heap(int capacity) {
            heap = new int[capacity];
            size = 0;
        }

        // Method to insert a new element into the heap
        public void insert(int value) {
            if (size == heap.length) {
                System.out.println("Heap is full. Cannot insert new element.");
                return;
            }
            heap[size] = value;
            heapifyUp(size);
            size++;
        }

        // Method to delete the root element from the heap
        public int delete() {
            if (size == 0) {
                System.out.println("Heap is empty. Cannot delete element.");
                return -1;
            }
            int root = heap[0];
            heap[0] = heap[size - 1];
            size--;
            heapifyDown(0);
            return root;
        }

        // Method to get the heap value at a specific index
        public int get(int index) {
            if (index < 0 || index >= size) {
                System.out.println("Invalid index. Cannot get heap value.");
                return -1;
            }
            return heap[index];
        }

        // Method to heapify up
        private void heapifyUp(int index) {
            int parentIndex = (index - 1) / 2;
            if (index > 0 && heap[parentIndex] > heap[index]) {
                swap(parentIndex, index);
                heapifyUp(parentIndex);
            }
        }

        // Method to heapify down
        private void heapifyDown(int index) {
            int leftChildIndex = 2 * index + 1;
            int rightChildIndex = 2 * index + 2;
            int smallest = index;
            if (leftChildIndex < size && heap[leftChildIndex] < heap[smallest]) {
                smallest = leftChildIndex;
            }
            if (rightChildIndex < size && heap[rightChildIndex] < heap[smallest]) {
                smallest = rightChildIndex;
            }
            if (smallest != index) {
                swap(smallest, index);
                heapifyDown(smallest);
            }
        }

        // Method to swap two elements in the heap
        private void swap(int i, int j) {
            int temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }
    }

    public static void main(String[] args) {
        Heap heap = new Heap(10);
        heap.insert(10);
        heap.insert(20);
        heap.insert(30);
        heap.insert(40);
        heap.insert(50);
        System.out.println("Heap elements: ");
        for (int i = 0; i < heap.size; i++) {
            System.out.print(heap.get(i) + " ");
        }
        System.out.println();
        System.out.println("Deleted element: " + heap.delete());
        System.out.println("Heap elements after deletion: ");
        for (int i = 0; i < heap.size; i++) {
            System.out.print(heap.get(i) + " ");
        }
    }
}