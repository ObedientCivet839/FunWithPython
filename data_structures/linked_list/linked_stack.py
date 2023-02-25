class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    class _Node:
        """Light weight, nonpublic class for storing a singly linked list node."""
        def __init__(self, elem, next):
            self._elem = elem
            self._next = next

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def __str__(self):
        res = []
        ptr = self._head
        while ptr:
            res.append(ptr._elem)
            ptr = ptr._next
        return " -> ".join(map(str, res))

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._elem
    
    def pop(self):
        """Remove and return the top element of the stack (i.e. LIFO).
        
        Raise Exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        temp = self._head._elem
        self._head = self._head._next
        self._size -= 1
        return temp

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


