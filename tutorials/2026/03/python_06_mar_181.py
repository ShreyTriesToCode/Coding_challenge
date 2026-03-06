# Monotonic Stack Example in Python

# Importing the required module
import heapq

# Function to find the k-th smallest element in an array
def find_kth_smallest(arr, k):
    # Create a monotonic stack to store the elements
    stack = []
    
    # Iterate through the array
    for num in arr:
        # If the stack is empty or the current number is smaller than the top of the stack
        while stack and num < stack[-1]:
            # Pop the top element from the stack
            heapq.heappop(stack)
        
        # Push the current number onto the stack
        heapq.heappush(stack, num)
    
    # Pop the top k elements from the stack
    for _ in range(k-1):
        heapq.heappop(stack)
    
    # Return the k-th smallest element
    return stack[0]

# Example usage:
if __name__ == "__main__":
    # Define the input array and k
    arr = [5, 3, 7, 2, 8, 1, 9]
    k = 3
    
    # Find the k-th smallest element
    result = find_kth_smallest(arr, k)
    
    # Print the result
    print("The", k, "th smallest element in the array is:", result)