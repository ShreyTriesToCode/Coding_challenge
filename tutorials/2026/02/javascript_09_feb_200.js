// Linked List Manipulation in JavaScript
// This file teaches you how to implement a linked list data structure and manipulate it using various operations like insertion, deletion, traversal.

class Node {
    // Define a class for Node that will be part of our LinkedList.
    constructor(data) {
        this.data = data;
        this.next = null; // A node has a reference (next pointer) to the next node in sequence.
    }
}

class LinkedList {
    // Define a class for LinkedList that will contain all the methods.
    constructor() {
        this.head = null; // Start with an empty linked list, represented by head set to null.
    }

    // Method to add new data at end of linked list
    append(data) {
        const newNode = new Node(data);
        if (!this.head) { // If the list is empty
            this.head = newNode;
            return; // Set the new node as head
        }
        let lastNode = this.head;
        while (lastNode.next) { // Traverse to the last node in the sequence.
            lastNode = lastNode.next;
        }
        lastNode.next = newNode; // Link the last node with a new one
    }

    // Method to add data at beginning of linked list
    prepend(data) {
        const newNode = new Node(data);
        if (!this.head) { // If list is empty
            this.head = newNode;
            return; // Set the new node as head
        }
        newNode.next = this.head; // Link a new node to existing head
        this.head = newNode; // Update the head
    }

    // Method to delete first occurrence of node with given data
    remove(data) {
        if (!this.head) return; // If list is empty
        if (this.head.data === data) { // If we are removing the head.
            this.head = this.head.next; // Update the head by pointing it to next node in sequence
            return;
        }
        let current = this.head;
        while (current.next) {
            if (current.next.data === data) {
                current.next = current.next.next; // Skip nodes after the one we want to remove.
                return;
            }
            current = current.next;
        }
    }

    // Method to print linked list
    printList() {
        const values = [];
        let currentNode = this.head;
        while (currentNode) {
            values.push(currentNode.data);
            currentNode = currentNode.next;
        }
        console.log(values); // Print the list of data.
    }
}

// Example usage:
const ll = new LinkedList();
ll.append(1);
ll.append(2);
ll.append(3);

console.log("Linked List:");
ll.printList(); // Output: [1, 2, 3]
ll.prepend(0);

console.log("After prepending 0:");
ll.printList(); // Output: [0, 1, 2, 3]

ll.remove(2);
ll.remove(1);

console.log("After removing 1 and 2:");
ll.printList(); // Output: [0, 3]