# Sliding Window Algorithm
## Overview
The sliding window algorithm is used to solve problems that require examining a subset of data from the original dataset.

## Code
```python
def max_sum_subarray(arr):
    # Initialize variables to store maximum sum and current sum
    max_sum = float('-inf')
    current_sum = 0

    # Initialize two pointers for the sliding window
    left = 0
    right = 0

    while right < len(arr):
        # Add element at the right pointer to the current sum
        current_sum += arr[right]

        # If the current sum is greater than the max sum, update max sum
        if current_sum > max_sum:
            max_sum = current_sum

        # If the current sum is less than 0, reset it and move the left pointer
        while current_sum < 0:
            current_sum -= arr[left]
            left += 1

        right += 1

    return max_sum


# Example usage:
arr = [1, -2, 3, -4, 5, -6]
print("Maximum sum of subarray is:", max_sum_subarray(arr))