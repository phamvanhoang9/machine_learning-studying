package dynamic_programming;

class Node {
    int data;
    Node next;
    Node prev;

    Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    Node head;

    DoublyLinkedList() {
        this.head = null;
    }

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
            newNode.prev = temp;
        }
    }

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

    public void insertAfter(Node prevNode, int data) {
        if (prevNode == null) {
            System.out.println("The given previos node cannot be null");
            return;
        }

        Node newNode = new Node(data);
        newNode.next = prevNode.next;
        newNode.prev = prevNode;
        prevNode.next = newNode;
    }

    public void deleteNode(int data) {
        Node current = head;
        if (current.data == data) {
            head = current.next;
            if (current.next != null) {
                current.next.prev = null;
            }
            return;
        }

        while (current != null) {
            if (current.next.data == data) {
                current.next = current.next.next;
                if (current.next != null) {
                    current.next.prev = current;
                }
                return;
            }
            current = current.next;
        }
    }

    public void reverse() {
        Node prev = null;
        Node current = head;
        Node next = null;
        while (current != null) {
            next = current.next;
            current.next = prev;
            if (prev != null) {
                prev.prev = current; // Fix: Assign 'prev' to 'current' node's 'prev' pointer instead of 'next' pointer
            }
            prev = current;
            current = next;
        }
        head = prev;
    }

    void rotate(int k) {
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
        head.prev = fast;
        head = slow.next;
        slow.next = null;
    }

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
}


public class double_linked_list {
    public static void main(String[] args) {
        DoublyLinkedList dl = new DoublyLinkedList();
        
        dl.addNode(1);
        dl.addNode(2);
        dl.addNode(3);
        dl.addNode(4);
        dl.addNode(5);
        dl.printList();
        dl.insertAfter(dl.searchNode(3), 9);
        dl.printList();
        dl.deleteNode(9);
        dl.printList();
        dl.reverse();
        dl.printList();
        dl.rotate(3);
        dl.printList();
    }
    
}
