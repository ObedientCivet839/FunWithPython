from heapq import heappop, heappush, heapify

def manual_test():
    h = []

    # add tuples into the heap
    heappush(h, (1,3,2))
    heappush(h, (3,7,2))
    heappush(h, (2,5,4))
    heappush(h, (6,3,1))


    while h:
        print(heappop(h))

    # output:
    # (1, 3, 2)
    # (2, 5, 4)
    # (3, 7, 2)
    # (6, 3, 1)

def heapify_test():
    a = [(1,2), (3,2), (4,2), (10,6), (6,7), (5,4)]
    heapify(a)
    while a:
        print(heappop(a))


from dataclasses import dataclass, field
from typing import Any
import itertools

@dataclass(order=True, unsafe_hash=True)
class PrioritizedItem:
    priority: int
    item: str=field(compare=False)
    
    

REMOVED='<removed-task>'

class Queue:
    pq = []
    entry_finder = {}
    counter = itertools.count()
    
    def add_task(self, task):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [task.priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)  # push the entry into the heap
    
    def remove_task(self, task):
        'Mark an existing task as REMOVED.'
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED
    
    def pop_task(self):
        'Remove and return the lowest priority task.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

def test():
    i1 = PrioritizedItem(3, 'Study')
    i2 = PrioritizedItem(2, 'Eat')
    i3 = PrioritizedItem(1, 'Sleep')
    
    q = Queue()
    q.add_task(i1)
    q.add_task(i2)
    q.add_task(i3)
    
    for i in range(3):
        print(q.pop_task())
    

# heapify_test()
test()