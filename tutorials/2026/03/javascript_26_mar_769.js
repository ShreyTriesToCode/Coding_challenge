// Monotonic Stack Algorithm in JavaScript
// This algorithm is used for finding the next smaller element to the right in an array.

function nextSmallerRight(arr) {
    let stack = [];
    let result = new Array(arr.length).fill(-1);
    // Iterate through the array from left to right.
    for (let i = 0; i < arr.length; i++) {
        // While the stack is not empty and the top element of the stack is greater than or equal to the current element,
        // pop all elements from the stack until we find an element that is smaller than the current element.
        while (stack.length > 0 && arr[stack[stack.length - 1]] >= arr[i]) {
            stack.pop();
        }
        // If the stack is not empty, update the result array with the index of the smallest element in the stack.
        if (stack.length > 0) {
            result[i] = stack[stack.length - 1];
        }
        // Push the current index onto the stack.
        stack.push(i);
    }
    return result;
}

// Example usage:
let arr = [5, 3, 8, 2, 9];
console.log(nextSmallerRight(arr));