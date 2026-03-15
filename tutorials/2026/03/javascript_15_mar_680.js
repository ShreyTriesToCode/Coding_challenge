// Sliding Window Algorithm in JavaScript
// This algorithm is used to find the maximum sum of a subarray within a given array.

function maxSumSubarray(arr) {
    // Initialize variables to store the current window's sum and its maximum sum.
    let windowSum = 0;
    let maxSum = -Infinity;

    // Initialize two pointers for the sliding window, one at the start and one at the end.
    let left = 0;
    let right = 0;

    // Continue iterating through the array until the right pointer reaches the end of the array.
    while (right < arr.length) {
        // Add the element at the right pointer to the current window's sum.
        windowSum += arr[right];

        // Update the maximum sum if the current window's sum is greater than the maximum sum found so far.
        maxSum = Math.max(maxSum, windowSum);

        // If the current window's sum becomes negative, remove elements from the left of the window to make it positive again.
        while (windowSum < 0 && left <= right) {
            windowSum -= arr[left];
            left++;
        }

        // Move the right pointer one step to the right to expand the window.
        right++;

    }

    return maxSum;
}

// Example usage:
let arr = [-2, -3, 4, -1, -2, 1, 5, -3];
console.log(maxSumSubarray(arr)); // Output: 7