// Trie Data Structure Implementation in C++
#include <iostream>
#include <string>

using namespace std;

// Define a struct to represent a node in the trie
struct Node {
    int charIndex;
    bool isEndOfWord;
    Node* children[26];

    // Initialize the node with default values
    Node() {
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }
        isEndOfWord = false;
        charIndex = -1;
    }
};

// Define a class to represent the trie data structure
class Trie {
private:
    Node* root;

public:
    // Constructor to initialize the trie with an empty root node
    Trie() {
        root = new Node();
    }

    // Destructor to clean up memory when the trie is no longer needed
    ~Trie() {
        destroyTrie(root);
    }

    // Insert a word into the trie
    void insert(const string& word) {
        int index = 0;
        for (char c : word) {
            if (!children(root, c)) {
                children(root, c) = new Node();
            }
            root = children(root, c);
            index++;
        }

        // Mark the end of the word
        root->isEndOfWord = true;
    }

    // Search for a word in the trie
    bool search(const string& word) {
        int index = 0;
        Node* current = root;

        for (char c : word) {
            if (!children(current, c)) {
                return false; // Word not found
            }
            current = children(current, c);
            index++;
        }

        // Return true if the end of the word is marked
        return current->isEndOfWord;
    }

    // Check if a prefix exists in the trie
    bool startsWith(const string& prefix) {
        int index = 0;
        Node* current = root;

        for (char c : prefix) {
            if (!children(current, c)) {
                return false; // Prefix not found
            }
            current = children(current, c);
            index++;
        }

        // Return true if we've reached the end of a word
        return true;
    }

private:
    // Helper function to create a new node or retrieve an existing one
    Node* children(Node* parent, char c) {
        int charIndex = c - 'a';
        if (charIndex >= 0 && charIndex < 26) {
            if (!parent->children[charIndex]) {
                return parent->children[charIndex] = new Node();
            }
            return parent->children[charIndex];
        }

        // If the character is not valid, return nullptr
        return nullptr;
    }

    // Helper function to destroy a subtree rooted at a given node
    void destroyTrie(Node* node) {
        if (node != nullptr) {
            for (int i = 0; i < 26; i++) {
                destroyTrie(node->children[i]);
            }
            delete node;
        }
    }

    // Test the trie with some example words
};

// Main function to test the trie
int main() {
    Trie trie;

    trie.insert("apple");
    trie.insert("banana");

    cout << boolalpha;
    cout << "