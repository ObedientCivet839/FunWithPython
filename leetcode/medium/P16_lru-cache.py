### PROBLEM STATEMENT
# https://leetcode.com/problems/lru-cache/

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# k1: v1
# k2: v2

# 1: 1
# 2: 3
# 1-> 1

# 1: 1
# 3: 3

# Q: 2, 3
# - TBD: 

# Heap - Priority Queue

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4


key priority queue:
3 -> 4
4 -> 5

# Method 2
from time import time

class TimeBoundedLRU:
    "LRU Cache that invalidates and refreshes old entries."

    def __init__(self, func, maxsize=128, maxage=30):
        self.cache = OrderedDict()      # { args : (timestamp, result)}
        self.func = func
        self.maxsize = maxsize
        self.maxage = maxage

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            timestamp, result = self.cache[args]
            if time() - timestamp <= self.maxage:
                return result
        result = self.func(*args)
        self.cache[args] = time(), result
        if len(self.cache) > self.maxsize:
            self.cache.popitem(0)
        return result

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if len(self.values) == self.capacity:
                self.values.popitem(last=False)
        else:
            self.values.pop(key)
        self.values[key] = value
# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class LRUCache:
    def __init__(self, capacity: int):
        self._cap = capacity
        # Least recently used is in the back
        self._lru = []
        self._map = {}

    def get(self, key: int) -> int:
        #print("get: key:", key)
        #print("get: lru:", self._lru)
        # TODO: Optimize
        if key in self._map:
            self.update_cache(key)
            return self._map[key]
        return -1
    
    def update_cache(self, key: int) -> None:
        if key in self._map:
            self._lru.remove(key)
        self._lru.insert(0, key)

    def put(self, key: int, value: int) -> None:
        #print("put: key:", key, ", val:", value)
        # Just update the key
        if key in self._map:
            self.update_cache(key)
            self._map[key] = value
            return
        # Evict and update
        if len(self._lru) >= self._cap:
            # Pop from the end of the list
            old_key = self._lru.pop()
            del self._map[old_key]
        self.update_cache(key)
        self._map[key] = value
        #self._lru.append(key)
        #self._lru.remove(key)
        #print("map:", self._map)
        #print("lru:", self._lru)


### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            nums: list[int]
            expected: int

        testcases = [
            TestCase(
                name="1",
                nums = 
                expected = 
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.X(tc.nums, tc.targets)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

def main():
    s = Solution()
    print(s)

if __name__ == '__main__':
    main()
    unittest.main()