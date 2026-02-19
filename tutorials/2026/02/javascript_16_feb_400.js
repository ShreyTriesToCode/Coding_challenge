// This JavaScript file teaches string manipulation using various methods and techniques.
// Understanding these concepts is essential for any aspiring web developer or programmer.

// Define a function to convert a sentence to uppercase
function convertToUppercase(sentence) {
  // Use the toUpperCase() method to convert each character in the string to uppercase
  return sentence.toUpperCase();
}

// Define a function to replace all vowels with 'X'
function replaceVowelsWithX(sentence) {
  // Declare a variable to store the pattern for matching vowels
  const vowelPattern = /[aeiou]/i;
  
  // Use the replace() method to replace all occurrences of vowels with 'X'
  return sentence.replace(vowelPattern, 'X');
}

// Define a function to find and print all substrings that start with 'a' or 'A'
function findStartingWithA(sentence) {
  // Declare a variable to store the pattern for matching strings starting with 'a' or 'A'
  const startPattern = /^a[A-Za-z]+/i;
  
  // Use the match() method to find all matches of this pattern in the string
  const matches = sentence.match(startPattern);
  
  // If there are any matches, print them; otherwise, print a message indicating that no matches were found
  if (matches) {
    console.log('Found matching strings:');
    for (const match of matches) {
      console.log(match);
    }
  } else {
    console.log('No matching strings found.');
  }
}

// Define a function to find and return the length of all substrings that contain 'o' or 'O'
function findLengthOfMatchingSubstrings(sentence) {
  // Declare a variable to store the pattern for matching substrings containing 'o' or 'O'
  const oPattern = /o[A-Za-z]+/i;
  
  // Use the match() method to find all matches of this pattern in the string
  const matches = sentence.match(oPattern);
  
  // If there are any matches, return their lengths; otherwise, return -1
  if (matches) {
    return matches.map(match => match.length).reduce((a, b) => a + b, 0);
  } else {
    return -1;
  }
}

// Define an array of example sentences
const exampleSentences = [
  'Hello, World!',
  'This is a test sentence with multiple words and punctuation.',
  'The quick brown fox jumps over the lazy dog.',
  'No vowels here, let\'s see how replaceVowelsWithX handles that.'
];

// Test the functions using the example sentences
for (const sentence of exampleSentences) {
  console.log('Original Sentence:');
  console.log(sentence);
  
  console.log('\nUppercase');
  console.log(convertToUppercase(sentence));
  
  console.log('\nReplace Vowels with X');
  console.log(replaceVowelsWithX(sentence));
  
  console.log('\nFind Strings Starting With A or a');
  findStartingWithA(sentence);
  
  console.log('\nLength of Matching Substrings (contains O)');
  const result = findLengthOfMatchingSubstrings(sentence);
  if (result !== -1) {
    console.log(result);
  } else {
    console.log('No matching substrings found.');
  }
}