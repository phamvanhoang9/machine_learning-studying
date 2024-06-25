using namespace std;
#include <iostream>
#include <vector>


// Creat a Node class
class Node {
    public:
        int data;
        Node* next; // Pointer to the next node
        Node(int data) {
            this->data = data;
            this->next = NULL;
        }
};

// Create a LinkedList class
class LinkedList {
    public: 
        Node* head; // Pointer to the head of the linked list
        LinkedList() {
            this->head = NULL;
        } 

        // Add a node to the end of the linked list
        void append(int data) {
            Node* new_node = new Node(data);
            if (this->head == NULL) {
                this->head = new_node;
                return;
            }
            Node* current = this->head;
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = new_node;
        }

        // Search for a node in the linked list
        Node* search(int data) {
            Node* current = this->head;
            while (current != NULL) {
                if (current->data == data) {
                    return current;
                }
                current = current->next;
            }
            return NULL;
        }

        // Insert a node after a given node
        void insert_after(Node* node, int data) {
            Node* new_node = new Node(data);
            new_node->next = node->next;
            node->next = new_node;
        }

        // Delete a node from the linked list
        void delete_node(int data) {
            Node* current = this->head;
            if (current->data == data) {
                this->head = current->next;
                delete current;
                return;
            }
            while (current->next != NULL) {
                if (current->next->data == data) {
                    Node* temp = current->next;
                    current->next = current->next->next;
                    delete temp;
                    return;
                }
                current = current->next;
            }
        }

        // Print the linked list
        void print() {
            Node* current = this->head;
            while (current != NULL) {
                cout << current->data << " ";
                current = current->next;
            }
            cout << endl;
        }

        // Reverse the linked list
        void reverse() {
            Node* prev = NULL;
            Node* current = this->head;
            Node* next = NULL;
            while (current != NULL) {
                next = current->next;
                current->next = prev;
                prev = current;
                current = next;
            }
            this->head = prev;
        }

        // Check if the linked list is a palindrome
        bool is_palindrome() {
            Node* current = this->head;
            vector<int> data;
            while (current != NULL) {
                data.push_back(current->data);
                current = current->next;
            }
            int n = data.size();
            for (int i = 0; i < n/2; i++) {
                if (data[i] != data[n-i-1]) {
                    return false;
                }
            }
            return true;
        }

        // Find the middle node of the linked list
        Node* middle_node() {
            Node* slow = this->head;
            Node* fast = this->head;
            while (fast != NULL && fast->next != NULL) {
                slow = slow->next;
                fast = fast->next->next;
            }
            return slow;
        }

        // Merge two sorted linked lists
        static LinkedList merge_sorted(LinkedList l1, LinkedList l2) {
            LinkedList merged;
            Node* current1 = l1.head;
            Node* current2 = l2.head;
            while (current1 != NULL && current2 != NULL) {
                if (current1->data < current2->data) {
                    merged.append(current1->data);
                    current1 = current1->next;
                } else {
                    merged.append(current2->data);
                    current2 = current2->next;
                }
            }
            while (current1 != NULL) {
                merged.append(current1->data);
                current1 = current1->next;
            }
            while (current2 != NULL) {
                merged.append(current2->data);
                current2 = current2->next;
            }
            return merged;
        }

        // Remove duplicates from a sorted linked list
        void remove_duplicates() {
            Node* current = this->head;
            while (current != NULL && current->next != NULL) {
                if (current->data == current->next->data) {
                    Node* temp = current->next;
                    current->next = current->next->next;
                    delete temp;
                } else {
                    current = current->next;
                }
            }
        }

        // Rotate the linked list by k positions
        void rotate(int k) {
            Node* current = this->head;
            int n = 0;
            while (current != NULL) {
                n++;
                current = current->next;
            }
            k = k % n;
            if (k == 0) {
                return;
            }
            Node* slow = this->head;
            Node* fast = this->head;
            for (int i = 0; i < k; i++) {
                fast = fast->next;
            }
            while (fast->next != NULL) {
                slow = slow->next;
                fast = fast->next;
            }
            fast->next = this->head;
            this->head = slow->next;
            slow->next = NULL;
        }
};

int main() {
    LinkedList l;
    l.append(1);
    l.append(2);
    l.append(3);
    l.append(4);
    l.append(5);
    l.append(6);
    l.append(7);
    l.append(8);
    l.print();
    l.rotate(3);
    l.print();
    l.reverse();
    l.print();
    l.insert_after(l.search(5), 9);
    l.print();
    l.delete_node(9);
    l.print();
    return 0;
}