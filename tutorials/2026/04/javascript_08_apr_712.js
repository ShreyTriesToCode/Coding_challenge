// Two Pointers Tutorial in JavaScript
// This script demonstrates the use of two pointers for common problems such as finding duplicates in an array, removing duplicates from an array, and swapping elements without using a temporary variable.

function findDuplicates(arr) {
    // Create an empty set to store unique elements
    let uniqueSet = new Set();
    
    // Iterate over each element in the input array
    for (let i = 0; i < arr.length; i++) {
        // If the current element is already in the set, it's a duplicate
        if (uniqueSet.has(arr[i])) {
            console.log(`Duplicate found: ${arr[i]}`);
        } else {
            // Add the current element to the set
            uniqueSet.add(arr[i]);
        }
    }
}

function removeDuplicates(arr) {
    // Create an empty object to store elements we've seen so far
    let seen = {};
    
    // Iterate over each element in the input array
    for (let i = 0; i < arr.length; i++) {
        // If we've seen this element before, skip it
        if (seen[arr[i]]) {
            continue;
        } else {
            // Add the current element to the 'seen' object
            seen[arr[i]] = true;
        }
    }
    
    // Return an array with duplicates removed
    return Object.keys(seen);
}

function swapElements(arr, i, j) {
    // Swap elements at indices i and j without using a temporary variable
    [arr[i], arr[j]] = [arr[j], arr[i]];
}

// Example usage:
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log("Original array:");
console.log(numbers);

findDuplicates(numbers);
removeDuplicates(numbers);
console.log("Array with duplicates removed:");
console.log(removeDuplicates(numbers));

// Swap elements at indices 0 and 3
let swappedNumbers = numbers.slice();
swapElements(swappedNumbers, 0, 3);
console.log("Array after swapping elements at indices 0 and 3:");
console.log(swappedNumbers);