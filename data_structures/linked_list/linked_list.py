class LinkedList:
    """Implementation of a singly linked list."""

    class _Node:
        """Light weight, nonpublic class for storing a singly linked list node."""
        def __init__(self, elem, next):
            self._elem = elem
            self._next = next

    def __init__(self):
        """Create an empty list."""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def __str__(self):
        res = []
        ptr = self._head
        while ptr:
            res.append(ptr._elem)
            ptr = ptr._next
        return " -> ".join(map(str, res))

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0
    
    def front(self):
        """Return (but do not remove) the element at the front of the list.
        
        Raise Exception if the list is empty.
        """
        if self.is_empty():
            raise Exception('List is empty')
        return self._head._elem
    
    def end(self):
        """Return (but do not remove) the element at the end of the list.
        
        Raise Exception if the list is empty.
        """
        if self.is_empty():
            raise Exception('List is empty')
        return self._tail._elem
    
    def remove_front(self):
        """Remove and return the first element of the list (i.e. FIFO).
        
        Raise Exception if the list is empty.
        """
        if self.is_empty():
            raise Exception('List is empty')
        temp = self._head._elem
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return temp

    def append(self, e):
        """Add element e to the back of the list."""
        n = self._Node(e, None)
        if self.is_empty():
            self._head = n
        else:
            self._tail._next = n
        self._tail = n
        self._size += 1

    def prepend(self, e):
        """Add element e to the front of the list."""
        self._head = self._Node(e, self._head)
        self._size += 1

    @classmethod
    def from_array(cls, elems):
        """"Return a LinkedList with the provided elements.

        The order of element in elems will be the order of insertion to the list.
        For example, if elems=[1,2,3,4], the linked list will have the order: 4->3->2->1.
        The list in the order of FIFO is [4,3,2,1] where 1 will be the first one to pop.
        
        Return an empty list if elems is None or is an empty list.
        """
        new_list = LinkedList()
        if not elems:
            return new_list
        for e in elems:
            new_list.append(e)
        return new_list

    # https://leetcode.com/problems/reverse-linked-list/
    def reverse(self):
        if len(self) < 2:
            return
        self._tail = self._head
        prev = self._head
        curr = self._head._next
        prev._next = None
        while curr:
            next = curr._next
            curr._next = prev
            prev = curr
            curr = next
        self._head = prev

    def reverse_recursive(self):
        """Return the reverse of this linked list.
        
        Use recursion.
        """
        new_head, new_tail = self.reverse_helper(self._head)
        self._head = new_head
        self._tail = new_tail
    
    def reverse_helper(self, head):
        """Helper of reverse().
        
        Reverse the list in place (destructive).
        Use recursion to reverse the rest of the list and then 
        link the node with the new tail.
        """
        if not head or not head._next:
            return head, head
        next = head._next
        head._next = None
        new_head, new_tail = self.reverse_helper(next)
        new_tail._next = head
        # current head becomes the new tail.
        return new_head, head

class Algorithms:
    # TODO
    # https://leetcode.com/problems/palindrome-linked-list/
    @classmethod
    def palindrome_linked_list(cls, linked_list):
        pass

    # TODO
    # https://leetcode.com/problems/odd-even-linked-list/
    @classmethod
    def odd_even_linked_list(cls, linked_list):
        pass
    
    # TODO
    # https://leetcode.com/problems/linked-list-random-node/
    @classmethod
    def random_node_linked_list(cls, linked_list):
        pass

    # TODO
    # https://leetcode.com/problems/delete-node-in-a-linked-list/
    @classmethod
    def delete_node_in_linked_list(cls, linked_list):
        pass



