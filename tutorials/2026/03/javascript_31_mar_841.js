// Prefix Sum in JavaScript
// == Definition ==
// The prefix sum of an array is the cumulative sum of its elements.

class PrefixSum {
  /**
   * Initialize the class with an empty prefix sum array.
   */
  constructor() {
    this.prefixSum = [];
  }

  /**
   * Calculate the prefix sum for the given input array.
   *
   * @param {number[]} nums - Input array of numbers.
   */
  calculatePrefixSum(nums) {
    // Initialize the prefix sum array with the first element of the input array
    this.prefixSum[0] = nums[0];
    // Iterate over each element in the input array (starting from the second element)
    for (let i = 1; i < nums.length; i++) {
      // Calculate the cumulative sum by adding the current element to the previous prefix sum
      this.prefixSum[i] = this.prefixSum[i - 1] + nums[i];
    }
  }

  /**
   * Get the nth prefix sum in the array.
   *
   * @param {number} n - Index of the prefix sum (0-based).
   * @returns {number} The nth prefix sum value.
   */
  getPrefixSum(n) {
    // Check if the index is within bounds
    if (n >= this.prefixSum.length) {
      throw new Error("Index out of bounds");
    }
    return this.prefixSum[n];
  }

  /**
   * Get a contiguous range of prefix sums from the given start and end indices.
   *
   * @param {number} start - Start index of the range (0-based).
   * @param {number} end - End index of the range (0-based).
   * @returns {number[]} An array of prefix sum values for the specified range.
   */
  getRangePrefixSums(start, end) {
    // Check if the indices are within bounds
    if (start > end || start >= this.prefixSum.length || end >= this.prefixSum.length) {
      throw new Error("Indices out of bounds");
    }
    return this.prefixSum.slice(start, end + 1);
  }
}

// Example usage:
const prefixSum = new PrefixSum();
prefixSum.calculatePrefixSum([1, 2, 3, 4, 5]);
console.log(prefixSum.getPrefixSum(0)); // Output: 1
console.log(prefixSum.getPrefixSum(1)); // Output: 3
console.log(prefixSum.getPrefixSum(2)); // Output: 6
console.log(prefixSum.getRangePrefixSums(0, 2)); // Output: [1, 3]