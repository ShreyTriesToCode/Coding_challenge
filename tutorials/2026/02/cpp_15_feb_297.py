// HashMap.cpp
// A C++ implementation of a basic HashMap data structure.

#include <iostream>
#include <string>

using namespace std;

// A simple hash map class with put, get and remove operations.
class HashMap {
private:
    int size;
    string** table;

public:
    // Constructor to initialize the hash map with a specified size.
    HashMap(int size) {
        this->size = size;
        table = new string*[size];
        for (int i = 0; i < size; i++) {
            table[i] = new string[10]; // each bucket can hold up to 10 elements
        }
    }

    // Destructor to free the memory allocated by the hash map.
    ~HashMap() {
        for (int i = 0; i < size; i++) {
            delete[] table[i];
        }
        delete[] table;
    }

    // Put a key-value pair into the hash map.
    void put(string key, string value) {
        int index = hash(key) % size;

        // If the bucket already has an element with the same key,
        // update its value.
        for (int i = 0; i < 10; i++) {
            if (!table[index][i].empty() && table[index][i] == key) {
                table[index][i] = value;
                return;
            }
        }

        // If the bucket is empty, add a new element.
        for (int i = 0; i < 10; i++) {
            if (!table[index][i].empty()) {
                break;
            }
            table[index][i] = key + ":" + value;
        }
    }

    // Get the value associated with a given key from the hash map.
    string get(string key) {
        int index = hash(key) % size;

        for (int i = 0; i < 10; i++) {
            if (!table[index][i].empty() && table[index][i] == key) {
                return table[index][i];
            }
        }

        // If the key is not found, return an empty string.
        return "";
    }

    // Remove a key-value pair from the hash map.
    void remove(string key) {
        int index = hash(key) % size;

        for (int i = 0; i < 10; i++) {
            if (!table[index][i].empty() && table[index][i] == key) {
                table[index][i] = "";
                return;
            }
        }
    }

private:
    // Simple hash function to map a string to an index.
    int hash(string key) {
        int sum = 0;
        for (char c : key) {
            sum += c;
        }
        return sum % size;
    }
};

// Example usage of the HashMap class
int main() {
    HashMap map(10);

    // Put some key-value pairs into the hash map.
    map.put("apple", "red");
    map.put("banana", "yellow");
    map.put("orange", "orange");

    // Get values from the hash map.
    cout << map.get("apple") << endl;  // Outputs: red
    cout << map.get("banana") << endl;  // Outputs: yellow

    // Remove a key-value pair from the hash map.
    map