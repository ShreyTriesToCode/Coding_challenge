# Dynamic Programming with Memoization
=====================================

In this example, we will implement the Fibonacci sequence using dynamic programming with memoization.

```python
def fibonacci(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to calculate.
        memo (dict): A dictionary to store previously calculated values. Defaults to {}.
        
    Returns:
        int: The nth Fibonacci number.
    """

    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if the value for n is already in memo
    if n not in memo:
        # If not, calculate it and store it in memo
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return the calculated value
    return memo[n]

# Example usage:
print(fibonacci(10))  # Output: 55