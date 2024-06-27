using namespace std;
#include <iostream>

class Node {
public:
    int data;
    Node* next;
    Node* prev;
    Node(int data) {
        this->data = data;
        this->next = NULL;
        this->prev = NULL;
    }
};

class DoublyLinkedList {
public:
    Node* head;
    DoublyLinkedList() {
        this->head = NULL;
    }

    void add(int data) {
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
        new_node->prev = current;
    }

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

    void insert_after(Node* node, int data) {
        Node* new_node = new Node(data);
        new_node->next = node->next;
        if (node->next != NULL) {
            node->next->prev = new_node;
        }
        node->next = new_node;
        new_node->prev = node;
    }

    void delete_node(int data) {
        Node* current = this->head;
        if (current->data == data) {
            this->head = current->next;
            if (current->next != NULL) {
                current->next->prev = NULL;
            }
            delete current;
            return;
        }
        while (current != NULL) {
            if (current->next->data == data) {
                Node* temp = current->next;
                current->next = current->next->next;
                if (current->next != NULL) {
                    current->next->prev = current;
                }
                delete temp;
                return;
            }
            current = current->next;
        }
    }

    void reverse() {
        Node* prev = NULL;
        Node* current = this->head;
        Node* next = NULL;
        while (current != NULL) {
            next = current->next;
            current->next = prev;
            //Check if prev is Null
            if (prev != NULL) {
                prev->prev = current;
            }
            prev = current;
            current = next;
        }
        this->head = prev;
    }

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
        this->head->prev = fast;
        this->head = slow->next;
        slow->next = NULL;

    }

    void print() {
        Node* current = this->head;
        while (current != NULL) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }
};

int main() {
    DoublyLinkedList dl;
    dl.add(1);
    dl.add(2);
    dl.add(3);
    dl.add(4);
    dl.add(5);
    dl.print();
    dl.insert_after(dl.search(3), 9);
    dl.print();
    dl.delete_node(3);
    dl.print();
    dl.reverse();
    dl.print();
    dl.rotate(2);
    dl.print();

    return 0;
}