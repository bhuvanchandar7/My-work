class BoundedStack:
    def __init__(self, capacity):
        '''
        Initializes a BoundedStack object with the specified capacity.
        Input:
            - capacity (int): Maximum capacity of the stack
        '''
        self.capacity = capacity
        self.items = []  # List to store items in the stack

    def push(self, item):
        '''
        Pushes an item onto the stack.
        Input:
            - item: Item to push onto the stack
        Returns:
            - bool: True if the item was successfully pushed, False otherwise
        '''
        if len(self.items) < self.capacity:
            self.items.append(item)
            return True
        else:
            print("Stack is full, cannot push more items.")
            return False

    def pop(self):
        '''
        Pops an item from the stack.
        Returns:
            - item: Item popped from the stack, or None if the stack is empty
        '''
        if self.items:
            return self.items.pop()
        else:
            print("Stack is empty, cannot pop.")
            return None

    def sealed(self):
        '''
        Checks if the stack is sealed, i.e., contains identical elements.
        Returns:
            - bool: True if the stack is sealed, False otherwise
        '''
        if len(self.items) == 3:
            first_element = self.items[0]
            for element in self.items[1:]:
                if element != first_element:
                    return False
            return True
        else:
            return False

    def is_empty(self):
        '''
        Checks if the stack is empty.
        Returns:
            - bool: True if the stack is empty, False otherwise
        '''
        return len(self.items) == 0

    def is_full(self):
        '''
        Checks if the stack is full.
        Returns:
            - bool: True if the stack is full, False otherwise
        '''
        return len(self.items) == self.capacity
