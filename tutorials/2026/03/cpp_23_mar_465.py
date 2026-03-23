// Divide and Conquer program in C++

#include <iostream>

// Function to find the minimum element in an array using Merge Sort
int mergeSort(int arr[], int low, int high) {
    // Base case: If the length of the subarray is 1 or less, return it as it's already sorted
    if (low >= high)
        return;

    // Calculate the middle index to split the array into two halves
    int mid = (low + high) / 2;
    
    // Recursively call mergeSort on both halves of the array
    mergeSort(arr, low, mid);
    mergeSort(arr, mid + 1, high);

    // Merge sorted subarrays back together in a sorted manner
    merge(arr, low, mid, high);
}

// Function to merge two sorted subarrays into one sorted subarray
void merge(int arr[], int low, int mid, int high) {
    // Create temporary arrays to hold the left and right halves of the array
    int leftSize = mid - low + 1;
    int rightSize = high - mid;

    int* leftArr = new int[leftSize];
    int* rightArr = new int[rightSize];

    // Copy elements from the original array into their respective temporary arrays
    for (int i = 0; i < leftSize; i++)
        leftArr[i] = arr[low + i];
    for (int j = 0; j < rightSize; j++)
        rightArr[j] = arr[mid + 1 + j];

    // Initialize indices to keep track of the current position in both arrays
    int leftIndex = 0, rightIndex = 0;
    int k = low;

    // Merge smaller elements first and then larger ones
    while (leftIndex < leftSize && rightIndex < rightSize) {
        if (leftArr[leftIndex] <= rightArr[rightIndex]) {
            arr[k++] = leftArr[leftIndex++];
        } else {
            arr[k++] = rightArr[rightIndex++];
        }
    }

    // Copy any remaining elements from the left array
    while (leftIndex < leftSize)
        arr[k++] = leftArr[leftIndex++];

    // Copy any remaining elements from the right array
    while (rightIndex < rightSize)
        arr[k++] = rightArr[rightIndex++];
}

int main() {
    int arr[] = {5, 2, 8, 3, 1, 6, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, n - 1);

    // Print the sorted array
    for (int i = 0; i < n; i++)
        std::cout << arr[i] << " ";
    std::cout << std::endl;

    return 0;
}