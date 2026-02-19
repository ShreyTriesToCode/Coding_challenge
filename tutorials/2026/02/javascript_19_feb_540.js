// Knuth-Morris-Pratt algorithm implementation in JavaScript
function computePrefixFunction(pattern) {
    // Initialize the prefix function with zeros
    let m = pattern.length;
    let pi = new Array(m).fill(0);
    // Compute the prefix function values
    for (let i = 1; i < m; i++) {
        let j = pi[i - 1];
        while (j > 0 && pattern[j] !== pattern[i]) {
            j = pi[j - 1];
        }
        if (pattern[j] === pattern[i]) {
            j++;
        }
        pi[i] = j;
    }
    return pi;
}

function kmpSearch(text, pattern) {
    // Compute the prefix function values
    let m = pattern.length;
    let pi = computePrefixFunction(pattern);
    // Initialize the indices
    let n = text.length;
    let i = 0;  // Index of the text
    let j = 0;  // Index of the pattern
    while (i < n) {
        if (j === 0 || pattern[j] !== text[i]) {
            // If the current characters match, move to the next character
            if (pattern[j] === text[i]) {
                j++;
            }
            i++;
        } else {
            // If we have found a match, move to the next position in the pattern
            i += pi[j - 1];
            j = pi[j];
        }
        if (j === m) {
            console.log("Found a match at index " + (i - j));
            break;
        }
    }
}

// Test the KMP algorithm
let text = 'ABABDABACDABABCABAB';
let pattern = 'ABAB';
kmpSearch(text, pattern);