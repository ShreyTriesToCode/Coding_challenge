// String Hashing Example in C++
// 
// This program demonstrates the basic concept of string hashing using separate chaining and linear probing techniques.

#include <iostream>
using namespace std;

class Node {
    // Each node represents a bucket in the hash table
    int key;
    char data[100]; // Character array to store string data
    Node* next; // Pointer to the next node in the linked list

public:
    // Constructor to initialize the node with key and data
    Node(int k, char str[]) {
        key = k;
        strcpy(data, str);
        next = nullptr;
    }
};

class HashTable {
    // A hash table class to manage the nodes using separate chaining
    int size; // Size of the hash table
    Node** buckets; // Pointer array to access each bucket

public:
    // Constructor to initialize the hash table with given size
    HashTable(int s) {
        size = s;
        buckets = new Node*[size]; // Dynamically allocate memory for each bucket
        for (int i = 0; i < size; i++)
            buckets[i] = nullptr;
    }

    // Function to calculate the hash value using linear probing
    int hashFunction(char* str) {
        int h = 0;
        while (*str != '\0') { // Iterate through each character of the string
            h += *str++;
        }
        return h % size; // Calculate the index using modulo operation
    }

    // Function to insert a new node into the hash table
    void insert(char* key, char str[]) {
        int index = hashFunction(str); // Get the index for the given string

        if (buckets[index] == nullptr) { // If the bucket is empty, create a new node
            buckets[index] = new Node(0, str);
            return;
        }

        Node* current = buckets[index]; // Start from the head of the linked list
        while (current != nullptr && strcmp(current->key, key) != 0) {
            if (strcmp(current->next->key, key) == 0) { // If a collision occurs with existing node
                if (current->data[100] != '\0') { // Check if the string is already present
                    cout << "String already exists in the hash table." << endl;
                    return;
                }
                current->next = new Node(0, str); // Update the next pointer and insert a new node
            } else {
                current = current->next; // Move to the next node in the linked list
            }
        }

        if (current != nullptr && strcmp(current->key, key) == 0) { // If collision occurs with existing node
            if (strlen(str) > 100) { // Check if the string is too long
                cout << "String length exceeds maximum allowed." << endl;
                return;
            }
            strcpy(current->data, str); // Update the data of the existing node
        } else {
            current = new Node(key, str); // Create a new node and insert it into the linked list
        }
    }

    // Function to search for a string in the hash table
    bool search(char* key) {
        int index = hashFunction(key);
        Node* current = buckets[index];
        while (current != nullptr && strcmp(current->