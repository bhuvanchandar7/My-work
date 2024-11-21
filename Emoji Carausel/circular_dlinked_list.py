class Node:
    def __init__(self, data=None):
        """
        Initializes a Node object.

        Parameters:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        """
        Gets the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self.data

    def set_data(self, new_data):
        """
        Sets new data to be stored in the node.

        Parameters:
            new_data: The new data to be stored.
        """
        self.data = new_data

    def get_next(self):
        """
        Gets the reference to the next node.

        Returns:
            The reference to the next node.
        """
        return self.next

    def set_next(self, new_next):
        """
        Sets the reference to the next node.

        Parameters:
            new_next: The reference to the next node.
        """
        self.next = new_next

    def get_prev(self):
        """
        Gets the reference to the previous node.

        Returns:
            The reference to the previous node.
        """
        return self.prev

    def set_prev(self, new_prev):
        """
        Sets the reference to the previous node.

        Parameters:
            new_prev: The reference to the previous node.
        """
        self.prev = new_prev
        
class CircularDoublyLinkedList:
    def __init__(self):
        """
        Initializes a CircularDoublyLinkedList object.
        """
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
        self.max_size = 5
        
    def get_size(self):
        """
        Gets the current size of the circular doubly linked list.

        Returns:
            The current size of the circular doubly linked list.
        """
        return self.size
        
    def add_node(self, data, side):
        """
        Adds a new node with data to the circular doubly linked list.

        Parameters:
            data: The data to be stored in the new node.
            side (str): The side to add the node (left/right).

        Raises:
            Exception: If the carousel is full.
        """
        new_node = Node(data)
        if self.size != self.max_size:
            if not self.head:
                self.head = new_node
                self.tail = new_node
                self.current = new_node
                new_node.next = new_node
                new_node.prev = new_node
            else:
                if side.upper() == 'LEFT':
                    new_node.prev = self.current.prev
                    new_node.next = self.current
                    self.current.prev.next = new_node
                    self.current.prev = new_node
                    if self.current == self.head:
                        self.head = new_node
                if side.upper() == 'RIGHT':
                    new_node.prev = self.current
                    new_node.next = self.current.next                
                    self.current.next.prev = new_node
                    self.current.next = new_node
                    if self.current == self.tail:
                        self.tail = new_node
            self.size += 1
            self.current = new_node
        else:
            raise Exception("You cannot add emojis! Carousel is Full.")

    def remove_node(self):
        """
        Removes the current node from the circular doubly linked list.

        Raises:
            Exception: If the carousel is empty.
        """
        if self.size == 0:
            raise Exception("Carousel is empty")
        if self.size == 1:
            self.head = None
            self.tail = None
            self.current = None
        else:
            deleted_node = self.current
            if deleted_node == self.head:
                self.head = deleted_node.next
            if deleted_node == self.tail:
                self.tail = deleted_node.prev
            deleted_node.prev.next = deleted_node.next
            deleted_node.next.prev = deleted_node.prev
            self.current = deleted_node.prev  # Move current to the left of the deleted node
            del deleted_node
        self.size -= 1

    def get_current(self):
        """
        Gets the data stored in the current node.

        Returns:
            The data stored in the current node.

        Raises:
            Exception: If the list is empty.
        """
        if self.current is None:
            raise Exception("List is empty")
        return self.current.data
    
    def before(self):
        """
        Gets the data stored in the node before the current node.

        Returns:
            The data stored in the node before the current node.

        Raises:
            Exception: If the list is empty.
        """
        if self.current is None:
            raise Exception("List is empty")
        return self.current.get_prev().get_data()

    def after(self):
        """
        Gets the data stored in the node after the current node.

        Returns:
            The data stored in the node after the current node.

        Raises:
            Exception: If the list is empty.
        """
        if self.current is None:
            raise Exception("List is empty")
        return self.current.get_next().get_data()    

    def move_next(self):
        """
        Moves the current pointer to the next node.

        Raises:
            Exception: If the list is empty.
        """
        if self.current is None:
            raise Exception("List is empty")
        self.current = self.current.next

    def move_prev(self):
        """
        Moves the current pointer to the previous node.

        Raises:
            Exception: If the list is empty.
        """
        if self.current is None:
            raise Exception("List is empty")
        self.current = self.current.prev
