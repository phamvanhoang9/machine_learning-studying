
class Node:
    """ 
    An object for storing a single node in a linked list
    
    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class SinglyLinkedList:
    """ 
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head.
    Each node points to the next node in the list
    
    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.head = None 
        # Maintaining a count attribute allows for len() to be implemented in constant time
        self.__count = 0 # __count for private attribute

    def is_empty(self):
        """ 
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None 
    
    def __len__(self):
        """ 
        Returns the length of the linked list
        Takens O(1) time
        """

        return self.__count 
    
    def add(self, data):
        """
        Adds new Node containing data to head of the list
        Also called prepend
        Takes O(1) time
        """

        new_head = Node(data, next_node=self.head) # Create a new node with the data and the current head as next node
        self.head = new_head 
        self.__count += 1

    def __repr__(self):
        """ 
        Return a string representation of the list.
        Takes O(n) time.
        """

        nodes = []
        current = self.head 
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node 
        
        return '-> '.join(nodes)