// Sliding Window Algorithm in C++
#include <iostream>
#include <vector>

// Function to find the maximum sum of a subarray of size k
int maxSumSubarray(std::vector<int>& nums, int k) {
  int maxSum = 0;
  int windowSum = 0;
  int left = 0;
  int right = 0;

  // Initialize the window boundaries
  while (right < nums.size()) {
    // Add the next element to the window sum
    windowSum += nums[right];
    // Move the right boundary of the window
    right++;

    // If the window size is greater than k, remove the leftmost element
    if (right - left > k) {
      windowSum -= nums[left];
      left++;
    }

    // Update the maximum sum if the window sum is greater
    if (right - left == k && windowSum > maxSum) {
      maxSum = windowSum;
    }
  }

  return maxSum;
}

int main() {
  std::vector<int> nums = {1, 2, 3, 4, 5};
  int k = 3;

  std::cout << "Maximum sum of a subarray of size " << k << " is " << maxSumSubarray(nums, k) << std::endl;

  return 0;
}