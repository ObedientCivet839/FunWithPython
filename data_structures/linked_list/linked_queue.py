class LinkedQueue:
    """FIFO Queue implementation using a singly linked list for storage."""

    class _Node:
        """Light weight, nonpublic class for storing a singly linked list node."""
        def __init__(self, elem, next):
            self._elem = elem
            self._next = next

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def __str__(self):
        res = []
        ptr = self._head
        while ptr:
            res.append(ptr._elem)
            ptr = ptr._next
        return " -> ".join(map(str, res))

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._elem
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).
        
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        temp = self._head._elem
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return temp

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        n = self._Node(e, None)
        if self.is_empty():
            self._head = n
        else:
            self._tail._next = n
        self._tail = n
        self._size += 1

    @classmethod
    def from_array(cls, elems):
        """"Return a LinkedQueue with the provided elements.

        The order of element in elems will be the order of insertion to the queue.
        For example, if elems=[1,2,3,4], the linked list will have the order: 4->3->2->1.
        The queue in the order of FIFO is [4,3,2,1] where 1 will be the first one to pop.
        
        Return an empty queue if elems is None or is an empty list.
        """
        new_queue = LinkedQueue()
        if not elems:
            return new_queue
        for e in elems:
            new_queue.enqueue(e)
        return new_queue


