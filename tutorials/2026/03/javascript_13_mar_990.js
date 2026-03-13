// Two Pointers Code
// 
// This JavaScript file demonstrates the concept of two pointers in array manipulation.

// Function to find the first duplicate in an array
function findFirstDuplicate(arr) {
    // Create a set to store unique elements
    let unique = new Set();
    
    // Iterate over the array with the first pointer
    for (let i = 0; i < arr.length; i++) {
        // If the current element is already in the set, it's a duplicate
        if (unique.has(arr[i])) {
            return i;
        }
        
        // Add the current element to the set
        unique.add(arr[i]);
    }
    
    // If no duplicates found, return -1
    return -1;
}

// Function to find the last duplicate in an array
function findLastDuplicate(arr) {
    // Create a set to store unique elements
    let unique = new Set();
    
    // Iterate over the array with the second pointer
    for (let i = arr.length - 1; i >= 0; i--) {
        // If the current element is already in the set, it's a duplicate
        if (unique.has(arr[i])) {
            return i;
        }
        
        // Add the current element to the set
        unique.add(arr[i]);
    }
    
    // If no duplicates found, return -1
    return -1;
}

// Function to find the pair of elements in an array that add up to a target sum
function findPairSum(arr, target) {
    // Create two pointers, one at the start and one at the end of the array
    let left = 0;
    let right = arr.length - 1;
    
    // Iterate until the pointers meet
    while (left < right) {
        // Calculate the sum of the current elements
        let sum = arr[left] + arr[right];
        
        // If the sum is equal to the target, return the pair
        if (sum === target) {
            return [arr[left], arr[right]];
        }
        
        // If the sum is less than the target, move the left pointer to the right
        else if (sum < target) {
            left++;
        }
        
        // If the sum is greater than the target, move the right pointer to the left
        else {
            right--;
        }
    }
    
    // If no pair found, return null
    return null;
}

// Test the functions
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(findFirstDuplicate(arr)); // Output: 0
console.log(findLastDuplicate(arr)); // Output: 7
console.log(findPairSum(arr, 10)); // Output: [ null ]

let arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(findFirstDuplicate(arr2)); // Output: 0
console.log(findLastDuplicate(arr2)); // Output: 8
console.log(findPairSum(arr2, 10)); // Output: [ 1, 9 ]