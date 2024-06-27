package dynamic_programming;

// This is a linked list implementation in Java
// The linked list is a data structure that consists of a sequence of elements, each element points to the next element in the sequence
// The linked list is a dynamic data structure, which means that the size of the list can be changed during the execution of the program
// The linked list is a linear data structure, which means that the elements are stored in a sequence and each element has a unique position in the list


// Node class
class Node {
    int data;
    Node next;

    // Constructor
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// LinkedList class
class LinkedList {
    Node head;

    // Constructor
    LinkedList() {
        this.head = null;
    }

    // Method to add a new node to the linked list
    public void addNode(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }

    // Search a node in the linked list
    Node searchNode(int data) {
        Node current = head;
        while (current != null) {
            if (current.data == data) {
                return current;
            }
            current = current.next;
        }
        return null;
    }

    // Method to insert a new node after a given node
    public void insertAfter(Node prevNode, int data) {
        if (prevNode == null) {
            System.out.println("The given previous node cannot be null");
            return;
        }

        Node newNode = new Node(data);
        newNode.next = prevNode.next;
        prevNode.next = newNode;
    }

    // Method to delete a node from the linked list
    public void deleteNode(int data) {
        Node temp = head;
        Node prev = null;

        if (temp != null && temp.data == data) {
            head = temp.next;
            return;
        }

        while (temp != null && temp.data != data) {
            prev = temp;
            temp = temp.next;
        }

        if (temp == null) {
            System.out.println("The given node is not present in the linked list");
            return;
        }

        prev.next = temp.next;
    }

    // Method to reverse linked list
    public void reverse() {
        Node prevNode = null;
        Node currentNode = head;
        Node nextNode = null;
        while (currentNode != null) {
            nextNode = currentNode.next;
            currentNode.next = prevNode;
            prevNode = currentNode;
            currentNode = nextNode;
        }
        head = prevNode;
    }

    // Method to rotate the list with k times
    public void rotate(int k) {
        Node currentNode = head;
        int n = 0;
        while (currentNode != null) {
            n = n + 1;
            currentNode = currentNode.next;
        }
        k = k % n;
        if (k == 0) {
            return;
        }
        Node slow = head;
        Node fast = head;
        for (int i = 0; i < k; i++) {
            fast = fast.next;
        }
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        fast.next = head;
        head = slow.next;
        slow.next = null;
    }

    // Method to print the linked list
    public void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}

// Main class
public class linked_list {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.addNode(1);
        list.addNode(2);
        list.addNode(3);
        list.addNode(4);
        list.addNode(5);
        list.printList();
        list.insertAfter(list.searchNode(3), 9);
        list.printList();
        list.deleteNode(0);
        list.printList();
        list.deleteNode(3);
        list.printList();
        list.reverse();
        list.printList();
        list.rotate(2);
        list.printList();
    }
}