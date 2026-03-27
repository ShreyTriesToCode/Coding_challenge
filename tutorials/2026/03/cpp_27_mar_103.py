// Heap Operations in C++
#include <iostream>
using namespace std;

// Function to insert an element into the heap
void insert(int* arr, int n, int value) {
    // Add the new element at the end of the array
    arr[n] = value;
    // Call heapify_up to maintain the heap property
    heapify_up(arr, n);
}

// Function to extract the minimum element from the heap
int extract_min(int* arr, int n) {
    // If the heap is empty, return -1
    if (n == 0)
        return -1;
    // Store the minimum element
    int min = arr[0];
    // Swap the first and last elements of the array
    swap(arr[0], arr[n - 1]);
    // Call heapify_down to maintain the heap property
    heapify_down(arr, n - 1);
    return min;
}

// Function to heapify up an element in the heap
void heapify_up(int* arr, int i) {
    // If the current node is a leaf node, stop
    if (i == 0)
        return;
    // Calculate the parent index
    int parent = (i - 1) / 2;
    // If the current element is smaller than its parent, swap them
    if (arr[i] < arr[parent])
        swap(arr[i], arr[parent]);
    // Recursively heapify up
    heapify_up(arr, parent);
}

// Function to heapify down an element in the heap
void heapify_down(int* arr, int i) {
    // Initialize two pointers for the left and right children
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    // Find the smallest child
    int smallest = i;
    if (left < n && arr[left] < arr[smallest])
        smallest = left;
    if (right < n && arr[right] < arr[smallest])
        smallest = right;
    // If the smallest child exists and is smaller than the current node, swap them
    if (smallest != i) {
        swap(arr[i], arr[smallest]);
        // Recursively heapify down
        heapify_down(arr, smallest);
    }
}

// Function to print the heap elements
void print_heap(int* arr, int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    // Create a sample array of size 10
    int arr[10];
    // Initialize the heap elements with some values
    for (int i = 0; i < 10; i++) {
        if (i % 2 == 0)
            arr[i] = i;
        else
            arr[i] = 10 - i;
    }
    cout << "Initial Heap Elements: ";
    print_heap(arr, 10);
    // Insert some new elements into the heap
    insert(arr, 10, 15);
    insert(arr, 10, 20);
    cout << "Heap after inserting new elements: ";
    print_heap(arr, 10);
    // Extract the minimum element from the heap
    int min = extract_min(arr, 10);