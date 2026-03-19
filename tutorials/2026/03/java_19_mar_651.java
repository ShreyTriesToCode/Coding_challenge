import java.util.Arrays;

public class HeapOperations {

    // Heapify function to maintain the heap property
    private static void heapify(int[] arr, int n, int i) {
        int largest = i;  // Initialize largest as root
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        // Check if left child exists and is greater than root
        if (left < n && arr[left] > arr[largest])
            largest = left;

        // Check if right child exists and is greater than the current largest
        if (right < n && arr[right] > arr[largest])
            largest = right;

        // Change the root, if needed
        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            heapify(arr, n, largest);
        }
    }

    // Insert a new element into the heap
    private static void insert(int[] arr, int n, int key) {
        // Add key at the end of the array
        arr[n] = key;

        // Heapify the root node to maintain heap property
        heapify(arr, n + 1, 0);
    }

    // Delete the minimum element from the heap
    private static void delete(int[] arr, int n) {
        if (n > 0) {

            // Replace the root with last element in array
            int temp = arr[0];
            arr[0] = arr[n - 1];
            arr[n - 1] = temp;

            // Reduce heap size by one
            n--;

            // Heapify root to maintain heap property
            heapify(arr, n, 0);
        }
    }

    // Print the elements of the heap
    private static void printHeap(int[] arr, int n) {
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String[] args) {

        // Create a sample heap of size 5
        int[] arr = new int[10];
        Arrays.fill(arr, 99);

        // Insert elements into the heap (in ascending order)
        insert(arr, arr.length - 1, 4);
        insert(arr, arr.length - 1, 12);
        insert(arr, arr.length - 1, 7);
        insert(arr, arr.length - 1, 25);

        System.out.println("Initial Heap: ");
        printHeap(arr, arr.length);

        // Delete the minimum element from the heap
        delete(arr, arr.length);

        System.out.println("Heap after deletion of min element: ");
        printHeap(arr, arr.length);
    }
}