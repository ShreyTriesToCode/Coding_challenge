import java.util.*;

public class HeapOperations {
    // This program teaches heap operations, which are essential in many programming applications.
    // It is useful for understanding priority queues and algorithms that rely on heaps.

    public static void main(String[] args) {
        // Create a min heap
        MinHeap heap = new MinHeap();

        // Add elements to the heap
        heap.insert(10);
        heap.insert(20);
        heap.insert(5);
        heap.insert(3);
        heap.insert(8);

        // Print the heap
        System.out.println("Min Heap: " + heap.toString());

        // Remove the smallest element from the heap
        int min = heap.extractMin();
        System.out.println("Removed Min: " + min);

        // Add new elements to the heap
        heap.insert(15);
        heap.insert(12);

        // Print the updated heap
        System.out.println("Updated Min Heap: " + heap.toString());

        // Create a max heap
        MaxHeap maxHeap = new MaxHeap();

        // Add elements to the heap
        maxHeap.insert(10);
        maxHeap.insert(20);
        maxHeap.insert(5);
        maxHeap.insert(3);
        maxHeap.insert(8);

        // Print the heap
        System.out.println("Max Heap: " + maxHeap.toString());

        // Remove the largest element from the heap
        int max = maxHeap.extractMax();
        System.out.println("Removed Max: " + max);

        // Add new elements to the heap
        maxHeap.insert(15);
        maxHeap.insert(12);

        // Print the updated heap
        System.out.println("Updated Max Heap: " + maxHeap.toString());
    }
}

class Node {
    int value;
    Node left;
    Node right;

    public Node(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class MinHeap {
    private Node[] heap;
    private int size;

    public MinHeap() {
        this.heap = new Node[10];
        this.size = 0;
    }

    // Insert a new element into the heap
    public void insert(int value) {
        if (size == heap.length) {
            // If the heap is full, resize it
            heap = Arrays.copyOf(heap, heap.length * 2);
        }
        Node newNode = new Node(value);

        // Add the new node to the end of the heap
        int i = size++;
        heap[i] = newNode;

        // Bubble up the new node until it's at its correct position
        while (i > 0) {
            int parentIndex = (i - 1) / 2;
            if (heap[parentIndex].value >= heap[i].value) {
                break;
            }
            swap(parentIndex, i);
            i = parentIndex;
        }
    }

    // Remove and return the smallest element from the heap
    public int extractMin() {
        if (size == 0) {
            throw new RuntimeException("Heap is empty");
        }
        int min = heap[0].value;

        // Replace the root with the last node in the heap
        Node lastNode = heap[--size];
        heap[0] = lastNode;
        bubbleDown(0);

        return min;
    }

    // Bubble down from