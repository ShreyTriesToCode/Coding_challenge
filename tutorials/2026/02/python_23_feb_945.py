# Prefix Sum
"""
Prefix sum is a technique used to optimize the calculation of prefix sums in an array. Instead of calculating the sum of all elements up to a certain index, we store the sum of all elements up to that index in an array and reuse it as needed.

This script provides a function to calculate prefix sums and demonstrates how to use it to solve a common problem.
"""

def calculate_prefix_sum(arr):
    # Initialize an empty list to store the prefix sums
    prefix_sums = [0] * (len(arr) + 1)

    # Calculate the prefix sums
    for i in range(len(arr)):
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]

    return prefix_sums

def solve_problem(arr):
    # Calculate the prefix sums
    prefix_sums = calculate_prefix_sum(arr)

    # Find the maximum sum of subarray
    max_sum = max(prefix_sums)

    # Find the first and last occurrence of the maximum sum
    first_occurrence = prefix_sums.index(max_sum)
    last_occurrence = len(arr) - 1 - prefix_sums[::-1].index(max_sum)

    return max_sum, first_occurrence, last_occurrence

# Test the function
arr = [1, 2, 3, 4, 5]
max_sum, first_occurrence, last_occurrence = solve_problem(arr)
print(f"Maximum sum of subarray: {max_sum}")
print(f"First occurrence: {first_occurrence}")
print(f"Last occurrence: {last_occurrence}")