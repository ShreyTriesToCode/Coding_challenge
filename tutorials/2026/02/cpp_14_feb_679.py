#include <iostream>
#include <vector>
using namespace std;

// This program teaches about Monotonic Stack, a technique used in dynamic programming to solve problems.
// A monotonic stack is an array where each element is either greater than or equal to every other element.

class MonotonicStack {
    int* arr;
    int n;
    int start;

public:
    // Constructor for the class
    MonotonicStack(int arr[]) {
        this->arr = new int[n];
        this->n = n;
        this->start = 0;
        build();
    }

    // Method to build the monotonic stack
    void build() {
        for (int i = 1; i < n; i++) {
            if (arr[i] >= arr[start]) {
                start = i;
            }
            arr[n - i - 1] = arr[start];
        }
    }

    // Method to get the maximum element
    int getMax() {
        return arr[0];
    }

    // Method to update the stack
    void update(int index, int val) {
        if (val < arr[index]) {
            for (int i = start; i > index; i--) {
                arr[i + 1] = arr[i - 1];
            }
            start = index;
        } else {
            // Update the current element in O(1) time
            arr[start] = val;
            while (start < n && arr[start] >= arr[start + 1]) {
                start++;
            }
        }
    }

    // Destructor to free the allocated memory
    ~MonotonicStack() {
        delete[] arr;
    }
};

int main() {
    int arr[] = {5, 3, 8, 4, 2};
    MonotonicStack stack(arr);
    cout << "Maximum element is: " << stack.getMax() << endl; // Output: Maximum element is: 8
    stack.update(0, 10); // Update the first element to 10
    cout << "Updated maximum element is: " << stack.getMax() << endl; // Output: Updated maximum element is: 10
    return 0;
}