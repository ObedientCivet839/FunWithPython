from linked_list import LinkedList

class LinkedQueue(LinkedList):
    """FIFO Queue implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        super().__init__()
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Exception if the queue is empty.
        """
        return self.front()
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).
        
        Raise Exception if the queue is empty.
        """
        return self.remove_front()

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        self.append(e)

    # TODO(P2): Need to define this method for each child class
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


