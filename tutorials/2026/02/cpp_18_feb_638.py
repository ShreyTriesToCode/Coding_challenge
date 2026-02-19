#include <iostream>
#include <stack>
#include <queue>

// This program teaches the basic operations of stack and queue data structures.
// Understanding these data structures is essential in computer science as they are used in many algorithms and data structures.

class Stack {
private:
    std::stack<int> stack;
public:
    // Push an element onto the stack
    void push(int value) {
        stack.push(value);
    }

    // Pop the top element from the stack
    int pop() {
        if (is_empty()) {
            throw std::out_of_range("Stack is empty");
        }
        return stack.top();
    }

    // Check if the stack is empty
    bool is_empty() {
        return stack.empty();
    }

    // Get the top element from the stack without removing it
    int peek() {
        if (is_empty()) {
            throw std::out_of_range("Stack is empty");
        }
        return stack.top();
    }

    // Clear the entire stack
    void clear() {
        while (!is_empty()) {
            pop();
        }
    }
};

class Queue {
private:
    std::queue<int> queue;
public:
    // Enqueue an element onto the queue
    void enqueue(int value) {
        queue.push(value);
    }

    // Dequeue the front element from the queue
    int dequeue() {
        if (is_empty()) {
            throw std::out_of_range("Queue is empty");
        }
        return queue.front();
    }

    // Check if the queue is empty
    bool is_empty() {
        return queue.empty();
    }

    // Get the front element from the queue without removing it
    int peek() {
        if (is_empty()) {
            throw std::out_of_range("Queue is empty");
        }
        return queue.front();
    }

    // Clear the entire queue
    void clear() {
        while (!is_empty()) {
            dequeue();
        }
    }
};

int main() {
    Stack stack;
    Queue queue;

    // Push elements onto the stack and print their values
    for (int i = 1; i <= 5; ++i) {
        stack.push(i);
        std::cout << "Pushed " << i << " onto the stack" << std::endl;
    }

    // Pop elements from the stack and print their values
    while (!stack.is_empty()) {
        int value = stack.pop();
        std::cout << "Popped " << value << " from the stack" << std::endl;
    }

    // Enqueue elements onto the queue and print their values
    for (int i = 1; i <= 5; ++i) {
        queue.enqueue(i);
        std::cout << "Enqueued " << i << " onto the queue" << std::endl;
    }

    // Dequeue elements from the queue and print their values
    while (!queue.is_empty()) {
        int value = queue.dequeue();
        std::cout << "Dequeued " << value << " from the queue" << std::endl;
    }

    return 0;
}