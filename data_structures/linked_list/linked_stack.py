from linked_list import LinkedList

class LinkedStack(LinkedList):
    """LIFO Stack implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty stack."""
        super().__init__()
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self.prepend(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Exception if the stack is empty.
        """
        return self.front()
    
    def pop(self):
        """Remove and return the top element of the stack (i.e. LIFO).
        
        Raise Exception if the stack is empty.
        """
        return self.remove_front()

    @classmethod
    def from_array(cls, elems):
        """"Return a LinkedStack with the provided elements.

        The order of element in elems will be the order of insertion to the stack.
        For example, if elems=[1,2,3,4], the linked list will have the order: 1->2->3->4.
        The stack in the order of LIFO is [1, 2, 3, 4] where 4 will be the first one to pop.
        
        Return an empty stack if elems is None or is an empty list.
        """
        new_stack = LinkedStack()
        if not elems:
            return new_stack
        for e in elems:
            new_stack.push(e)
        return new_stack


