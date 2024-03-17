"""
Given a linked list of N nodes such that it may contain a loop.
A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.
Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

Your task is to complete the function removeLoop() which takes the head of the linked list as the input parameter. Simply remove the loop in the list (if present) without disconnecting any nodes from the list.
Note: The generated output will be 1 if your submitted code is correct.
"""

# Reference: [GeeksforGeeks](https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/)

# Node Class
class Node:
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None # Initialize head as None 

    def push(self, new_data):
        new_node = Node(new_data) # Create a new Node
        new_node.next = self.head # Make next of new Node as head
        self.head = new_node # Move the head to point to new Node

    def detectLoop(self):
        slow_p = self.head # Initialize slow pointer
        fast_p = self.head # Initialize fast pointer
        while(slow_p and fast_p and fast_p.next): # Traverse the list
            slow_p = slow_p.next # Move slow pointer one step
            fast_p = fast_p.next.next # Move fast pointer two steps
            if slow_p == fast_p:
                self.removeLoop(slow_p)
                return 1
        return 0

    def removeLoop(self, loop_node):
        ptr1 = self.head
        while(1):
            ptr2 = loop_node
            while(ptr2.next != loop_node and ptr2.next != ptr1):
                ptr2 = ptr2.next
            if ptr2.next == ptr1: # Break the loop
                break
            ptr1 = ptr1.next
        ptr2.next = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Driver Code
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(10)
    llist.push(4)
    llist.push(15)
    llist.push(20)
    llist.push(50)
    llist.head.next.next.next.next.next = llist.head.next.next
    llist.detectLoop()
    print("Linked List after removing loop")
    llist.printList()
