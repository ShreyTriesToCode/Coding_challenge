// Heap Operations in Java

import java.util.*;

public class HeapOperations {

    // Heap implementation using Binary Heap data structure
    class Heap {
        int[] heap;
        int size;

        public Heap(int capacity) {
            heap = new int[capacity];
            size = 0;
        }

        // Insert an element into the heap
        public void insert(int key) {
            if (size == heap.length) {
                System.out.println("Heap is full. Cannot insert element.");
                return;
            }
            heap[size++] = key;
            heapifyUp(size - 1);
        }

        // Delete the root element from the heap
        public int delete() {
            if (size == 0) {
                System.out.println("Heap is empty. Cannot delete element.");
                return -1;
            }
            int root = heap[0];
            heap[0] = heap[--size];
            heapifyDown(0);
            return root;
        }

        // Heapify up operation to maintain heap property
        private void heapifyUp(int i) {
            if (i == 0) {
                return;
            }
            int parent = (i - 1) / 2;
            if (heap[i] < heap[parent]) {
                // Swap elements
                int temp = heap[i];
                heap[i] = heap[parent];
                heap[parent] = temp;
                heapifyUp(parent);
            }
        }

        // Heapify down operation to maintain heap property
        private void heapifyDown(int i) {
            int smallest = i;
            int left = 2 * i + 1;
            int right = 2 * i + 2;

            if (left < size && heap[left] < heap[smallest]) {
                smallest = left;
            }
            if (right < size && heap[right] < heap[smallest]) {
                smallest = right;
            }

            if (smallest != i) {
                // Swap elements
                int temp = heap[i];
                heap[i] = heap[smallest];
                heap[smallest] = temp;
                heapifyDown(smallest);
            }
        }
    }

    public static void main(String[] args) {
        Heap heap = new Heap(10);

        // Insert elements into the heap
        heap.insert(10);
        heap.insert(20);
        heap.insert(30);
        heap.insert(15);
        heap.insert(25);

        // Delete elements from the heap
        System.out.println("Deleted element: " + heap.delete());
        System.out.println("Deleted element: " + heap.delete());
        System.out.println("Deleted element: " + heap.delete());
        System.out.println("Deleted element: " + heap.delete());
        System.out.println("Deleted element: " + heap.delete());

        // Try to delete from an empty heap
        heap.delete();
    }
}