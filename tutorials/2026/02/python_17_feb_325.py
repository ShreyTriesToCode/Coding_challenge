# Dynamic Programming Memoization in Python

This script teaches the concept of dynamic programming memoization using Python. Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and reusing them when the same inputs occur again.

```python
def fibonacci(n, memo={}):
    # Base cases: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if result is already in memo dictionary
    if n not in memo:
        # If not, calculate it and store in memo dictionary
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return result from memo dictionary
    return memo[n]

# Example usage: test with different inputs
print("Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Test optimization
import time

start_time = time.time()
result1 = fibonacci(30)
end_time = time.time()
print(f"Time to calculate F(30) without memoization: {end_time - start_time} seconds")

start_time = time.time()
result2 = fibonacci(30, {})
end_time = time.time()
print(f"Time to calculate F(30) with memoization: {end_time - start_time} seconds")