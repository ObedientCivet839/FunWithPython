class DoublyLinkedList:
    """A base class providing a doubly linked list representation."""
    class _Node:
        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty doubly linked list."""
        # Using sentinels to avoid special case.
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between 2 existing nodes and return new node."""
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """Delete nonsential node from the list and return its element."""
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        elem = node._elem
        node._prev = node._next = node._elem = None # deprecate node
        return elem
    
    def __str__(self):
        res = []
        ptr = self._header
        while ptr:
            if ptr._elem:
                res.append(str(ptr._elem))
            ptr = ptr._next
        return " -> ".join(res)

class LinkedDeque(DoublyLinkedList):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._header._next._elem # real item is after the head
    
    def last(self):
        """Return (but not remove) the element at the end of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._trailer._prev._elem # real item is before the trailer
    
    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)
    
    def delete_first(self):
        """Remove and return the element from the front of the deque.
        
        Raise Exception if the deque is empty.
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        
        Raise Exception if the deque is empty.
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self._trailer._prev)



