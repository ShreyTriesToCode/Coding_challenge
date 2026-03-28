// Prefix Sum in JavaScript
//=====================================

// Function to calculate the prefix sum of an array
function prefixSum(arr) {
    // Initialize the result array with the first element of the input array
    let result = new Array(arr.length).fill(0);
    result[0] = arr[0];

    // Iterate over the input array starting from the second element
    for (let i = 1; i < arr.length; i++) {
        // Calculate the prefix sum by adding the current element to the previous prefix sum
        result[i] = result[i - 1] + arr[i];
    }

    return result;
}

// Function to print an array
function printArray(arr) {
    // Use the console.log function to print the array
    console.log(arr);
}

// Example usage
let numbers = [1, 2, 3, 4, 5];
let prefixSumNumbers = prefixSum(numbers);
printArray(prefixSumNumbers);

numbers = [10, -20, 30, -40, 50];
prefixSumNumbers = prefixSum(numbers);
printArray(prefixSumNumbers);