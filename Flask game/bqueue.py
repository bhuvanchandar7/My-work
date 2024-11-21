class BoundedQueue:
    def __init__(self, capacity):
        """
        Initialize the BoundedQueue object.

        Args:
            capacity (int): Maximum capacity of the queue.

        Raises:
            AssertionError: If capacity is not an integer or if it's negative.
        """
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))
        self.__items = []
        self.__capacity = capacity

    def enqueue(self, item):
        """
        Add an item to the end of the queue.

        Args:
            item: The item to be added to the queue.

        Raises:
            Exception: If the queue is full.
        """
        if len(self.__items) >= self.__capacity:
            raise Exception('Error: Queue is full')
        self.__items.append(item)

    def dequeue(self):
        """
        Remove and return the item from the front of the queue.

        Returns:
            The item removed from the front of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items.pop(0)

    def isEmpty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.__items) == 0

    def isFull(self):
        """
        Check if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return len(self.__items) == self.__capacity

    def size(self):
        """
        Return the current size of the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self.__items)

    def capacity(self):
        """
        Return the maximum capacity of the queue.

        Returns:
            int: The maximum capacity of the queue.
        """
        return self.__capacity
