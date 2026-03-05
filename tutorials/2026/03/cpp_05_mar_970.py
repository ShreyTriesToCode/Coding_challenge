#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// Function to find maximum sum of a subarray of size k
int maxSumSubarray(std::vector<int>& arr, int k) {
    // Initialize the window start index
    int windowStart = 0;

    // Initialize the sum of the current window
    int windowSum = 0;

    // Initialize the maximum sum found so far
    int maxSum = 0;

    // Iterate over the array
    for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
        // Add the current element to the window sum
        windowSum += arr[windowEnd];

        // If the window size is greater than k, remove the first element of the window
        if (windowEnd >= k - 1) {
            windowSum -= arr[windowStart];
            windowStart++;
        }

        // Update the maximum sum found so far
        if (windowEnd >= k - 1) {
            maxSum = std::max(maxSum, windowSum);
        }
    }

    // Return the maximum sum found
    return maxSum;
}

int main() {
    // Create a sample array
    std::vector<int> arr = {-2, -3, 4, -1, -2, 1, 5, -3};

    // Specify the window size
    int k = 3;

    // Find the maximum sum of a subarray of size k
    int maxSum = maxSumSubarray(arr, k);

    // Print the result
    std::cout << "Maximum sum of a subarray of size " << k << ": " << maxSum << std::endl;

    return 0;
}