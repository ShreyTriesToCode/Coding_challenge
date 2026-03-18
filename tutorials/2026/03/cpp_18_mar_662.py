// Prefix Sum Explanation in C++
// This program demonstrates how to use the prefix sum technique
// to solve problems where we need to find an element's value 
// after performing operations on it.

#include <iostream>
#include <vector>

void calculatePrefixSum(std::vector<int>& nums) {
    // Initialize the first element of the prefix sum array with the first number in nums
    std::vector<int> prefixSum(nums.size(), 0);
    prefixSum[0] = nums[0];

    // Iterate over the numbers starting from the second one
    for (int i = 1; i < nums.size(); ++i) {
        // For each number, add its value to the previous element in the prefix sum array
        prefixSum[i] = prefixSum[i - 1] + nums[i];
    }

    return;
}

void solveProblem(std::vector<int> nums, int target) {
    // Find the index of the target element using binary search
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;

        // If the middle element equals the target, we found it
        if (nums[mid] == target) {
            std::cout << "Target found at index " << mid << std::endl;
            return;
        }

        // If the middle element is less than the target, move to the right half
        else if (nums[mid] < target) {
            left = mid + 1;
        }
        // If the middle element is greater than the target, move to the left half
        else {
            right = mid - 1;
        }
    }

    std::cout << "Target not found" << std::endl;
}

int main() {
    // Create a sample array of numbers
    std::vector<int> nums = {1, 2, 3, 4, 5};
    
    // Calculate the prefix sum for this array
    calculatePrefixSum(nums);
    
    // Find an element in the array using binary search with prefix sums
    solveProblem(nums, 7);

    return 0;
}