import java.util.PriorityQueue;

public class HeapOperations {
    public static void main(String[] args) {
        // Create a new min heap
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        System.out.println("Creating a min heap:");
        
        // Push elements onto the heap
        minHeap.add(10);
        minHeap.add(20);
        minHeap.add(5);
        System.out.println("Pushing 10, 20, and 5 into the min heap.");
        
        // Access the smallest element (head of the heap)
        System.out.println("Accessing the smallest element:");
        System.out.println(minHeap.peek());
        
        // Remove the smallest element
        System.out.println("Removing the smallest element:");
        System.out.println(minHeap.poll());
        
        // Push a new element onto the heap
        minHeap.add(15);
        System.out.println("Pushing 15 into the min heap.");
        
        // Peek at the smallest element again to see the effect of adding 15
        System.out.println("Accessing the smallest element after adding 15:");
        System.out.println(minHeap.peek());
    }
}