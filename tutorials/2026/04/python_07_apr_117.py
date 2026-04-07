# Prefix Sum Algorithm in Python
=====================================

The prefix sum algorithm is used to calculate the cumulative sum of elements in an array without having to iterate over the entire array multiple times. This can be particularly useful when working with large datasets.

### Step 1: Initialize the Array and Prefix Sum Array

```python
def prefix_sum(arr):
    # Get the length of the input array
    n = len(arr)
    
    # Create a new array to store the prefix sum values
    prefix_arr = [0] * (n + 1)
    
    # Initialize the prefix sum array with zeros
    for i in range(n):
        prefix_arr[i + 1] = arr[i]
```

### Step 2: Calculate Prefix Sum Values

```python
# Iterate over the input array and calculate the prefix sum values
for i in range(1, n):
    # For each element, add its value to the previous prefix sum value
    prefix_arr[i + 1] += arr[i]
```

### Step 3: Return the Prefix Sum Array

```python
# Return the prefix sum array
return prefix_arr
```

### Example Usage:

```python
def main():
    # Define a sample input array
    arr = [1, 2, 3, 4, 5]
    
    # Calculate the prefix sum array
    prefix_arr = prefix_sum(arr)
    
    # Print the prefix sum array
    print("Prefix Sum Array:", prefix_arr)

if __name__ == "__main__":
    main()
```

### Running the Example:

To run this code, save it to a file (e.g., `prefix_sum.py`) and execute it using Python:
```bash
python prefix_sum.py