# Two Pointers Technique in Python
# This script demonstrates the use of two pointers technique to solve a common problem.

def find_middle_node(head):
    # Initialize two pointers
    slow = head
    fast = head
    
    # Traverse the linked list
    while True:
        # Move the slow pointer one step at a time
        slow = slow.next
        
        # If the fast pointer reaches the end of the list, break
        if fast is None or fast.next is None:
            break
        
        # Move the fast pointer two steps at a time
        fast = fast.next.next
    
    # At this point, 'slow' and 'fast' meet at the middle node
    return slow

def find_middle_node_iterative(head):
    # Initialize two pointers
    slow = head
    fast = head
    
    # Traverse the linked list
    while True:
        # Move the slow pointer one step at a time
        slow = slow.next
        
        # If the fast pointer reaches the end of the list, break
        if fast is None or fast.next is None:
            break
        
        # Move the fast pointer two steps at a time
        fast = fast.next.next
    
    # At this point, 'slow' and 'fast' meet at the middle node
    return slow

# Create a linked list with 5 nodes: A, B, C, D, E
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Example usage:
print(find_middle_node(head).data)  # Output: 3

def find_middle_node_recursive(head):
    # Base case
    if head is None or head.next is None:
        return head
    
    # Recursive case for the first half of the list
    first_half = find_middle_node_recursive(head)
    
    # Calculate the middle node using recursion
    middle_node = first_half
    next_node = head
    while True:
        if next_node == middle_node:
            break
        else:
            next_node = next_node.next
    
    return middle_node

# Create a linked list with 5 nodes: A, B, C, D, E
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Example usage:
print(find_middle_node_recursive(head).data)  # Output: 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Runner example using the find_middle_node function
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    middle_node = find_middle_node(head)
    print("Middle node data:", middle_node.data)  # Output: Middle node data: 3