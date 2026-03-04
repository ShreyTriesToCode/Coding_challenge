public class SlidingWindow {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        int k = 3;
        System.out.println("Maximum sum of a subarray of size " + k + ": " + maxSum(nums, k));
    }

    /**
     * Returns the maximum sum of a subarray of size k in the given array.
     * 
     * @param nums the input array
     * @param k    the size of the subarray
     * @return the maximum sum of a subarray of size k
     */
    public static int maxSum(int[] nums, int k) {
        int n = nums.length;
        // Initialize the maximum sum and the current sum
        int maxSum = Integer.MIN_VALUE;
        int currentSum = 0;
        
        // Initialize the left and right pointers of the sliding window
        int left = 0;
        int right = 0;
        
        // Iterate over the array with the right pointer
        while (right < n) {
            // Add the element at the right pointer to the current sum
            currentSum += nums[right];
            
            // If the window size is greater than k, remove the element at the left pointer
            if (right - left + 1 > k) {
                currentSum -= nums[left];
                left++;
            }
            
            // Update the maximum sum if the current sum is greater
            if (right - left + 1 == k && currentSum > maxSum) {
                maxSum = currentSum;
            }
            
            // Move the right pointer to the next element
            right++;
        }
        
        return maxSum;
    }
}