// Binary Search Algorithm in C++
// Author: [Your Name]
// Date: [Today's Date]

#include <iostream>
using namespace std;

/**
 * Function to perform binary search on a sorted array.
 *
 * @param arr The input array to be searched.
 * @param target The value to be searched for in the array.
 * @param low The starting index of the array.
 * @param high The ending index of the array.
 * @return 0 if the element is not found, 1 if the element is found.
 */
int binarySearch(int arr[], int target, int low, int high) {
    // If the array is empty, return -1
    if (low > high)
        return -1;
    
    // Calculate the middle index of the array
    int mid = (low + high) / 2;
    
    // Check if the middle element matches the target
    if (arr[mid] == target)
        return mid; // Target found, return its index
    
    // If the middle element is greater than the target, search in the left half
    else if (arr[mid] > target)
        return binarySearch(arr, target, low, mid - 1);
    
    // If the middle element is less than the target, search in the right half
    else
        return binarySearch(arr, target, mid + 1, high);
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    int target;
    cout << "Enter a number to search for: ";
    cin >> target;
    
    // Perform binary search
    int index = binarySearch(arr, target, 0, n - 1);
    
    if (index != -1)
        cout << "Number found at index " << index << endl;
    else
        cout << "Number not found in the array" << endl;
    
    return 0;
}