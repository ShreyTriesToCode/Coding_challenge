// binary_search.cpp

// Binary Search Algorithm

// Function to perform binary search
int binarySearch(int arr[], int n, int target) {
    // Initialize two pointers, one at the start and one at the end
    int left = 0; // Left pointer
    int right = n - 1; // Right pointer

    // Continue the search until the two pointers meet
    while (left <= right) {
        // Calculate the middle index
        int mid = left + (right - left) / 2;

        // If the target is found, return its index
        if (arr[mid] == target) {
            return mid;
        }

        // If the target is less than the middle element, move the right pointer
        else if (arr[mid] > target) {
            right = mid - 1;
        }

        // If the target is greater than the middle element, move the left pointer
        else {
            left = mid + 1;
        }
    }

    // If the target is not found, return -1
    return -1;
}

// Function to print an array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to test the binary search function
void testBinarySearch() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 23;

    printf("Original array: ");
    printArray(arr, n);

    // Perform binary search
    int result = binarySearch(arr, n, target);

    if (result != -1) {
        printf("Target %d found at index %d\n", target, result);
    } else {
        printf("Target %d not found in the array\n", target);
    }
}

int main() {
    testBinarySearch();
    return 0;
}