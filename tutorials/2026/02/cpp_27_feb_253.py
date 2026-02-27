// String Hashing in C++
// ======================

#include <iostream>
#include <string>

// Function to calculate the hash of a string
int stringHash(const std::string& str) {
    // Initialize the hash value
    int hashValue = 0;

    // Calculate the length of the string
    int length = str.length();

    // Iterate over each character in the string
    for (int i = 0; i < length; i++) {
        // Convert the character to its ASCII value
        int asciiValue = str[i];

        // Calculate the hash value using the ASCII value
        // We use the formula: (hashValue * 31 + asciiValue) % 1000000007
        // This is a common hashing formula used in many string hashing algorithms
        hashValue = (hashValue * 31 + asciiValue) % 1000000007;
    }

    // Return the calculated hash value
    return hashValue;
}

// Function to calculate the hash of a character
int characterHash(char c) {
    // Convert the character to its ASCII value
    int asciiValue = static_cast<int>(c);

    // Calculate the hash value using the ASCII value
    // We use the formula: (hashValue * 31 + asciiValue) % 1000000007
    // This is a common hashing formula used in many string hashing algorithms
    int hashValue = (asciiValue * 31) % 1000000007;

    // Return the calculated hash value
    return hashValue;
}

int main() {
    // Test the stringHash function
    std::string str = "Hello World";
    int hashValue = stringHash(str);
    std::cout << "Hash value of '" << str << "': " << hashValue << std::endl;

    // Test the characterHash function
    char c = 'A';
    int hashValueChar = characterHash(c);
    std::cout << "Hash value of character '" << c << "': " << hashValueChar << std::endl;

    return 0;
}