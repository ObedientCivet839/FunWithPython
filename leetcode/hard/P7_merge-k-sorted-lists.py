### PROBLEM STATEMENT
# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @classmethod
    def toArray(cls, node):
        res  = []
        ptr = node
        while ptr:
            res.append(ptr.val)
            ptr = ptr.next
        return res

    @classmethod
    def toList(cls, arr):
        head = ListNode(0)
        node = head
        for v in arr:
            node.next = ListNode(v)
            node = node.next
        return head.next

class Solution1:
    def mergeKLists(self, lists: list[list[int]]) -> Optional[ListNode]:
        head = ListNode(0)
        N = len(lists)
        currIndex = [0] * N # store the current start of each list
        finished = False # finished if there is no items from each list
        newNode = head
        while not finished:
            minVal = 1000000 # set to max value
            minId = 0
            finished = True
            for i in range(N):
                ci = currIndex[i] # current index of the list i
                if ci < len(lists[i]):
                    finished = False
                    if lists[i][ci] < minVal:
                        minId = i
                        minVal = lists[i][ci]
            # create new node and attach node
            newNode.next = ListNode(minVal)
            newNode = newNode.next
            currIndex[minId] += 1 # increment id of the smallest list
        return head.next

class Solution2:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        N = len(lists)
        finished = False # finished if there is no items from each list
        newNode = head
        while not finished:
            minVal = 1000000 # set to max value
            minId = 0
            finished = True
            for i in range(N):
                if lists[i]:
                    finished = False
                    if lists[i].val < minVal:
                        minId = i
                        minVal = lists[i].val
            # BUG 1: If all lists are exhausted, break out of loop
            if finished:
                break
            # create new node and attach node
            newNode.next = ListNode(minVal)
            newNode = newNode.next
            lists[minId] = lists[minId].next # increment the list with the smallest item
        return head.next

from heapq import heappush, heappop

# Use heap
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        N = len(lists)

        if len(lists) == 0:
            return None

        for i in range(N):
            while lists[i]:
                # Just push all items to a heap
                heappush(heap, lists[i].val)
                lists[i] = lists[i].next
        
        head = ListNode(0) # use a dummy node
        node = head
        while heap:
            node.next = ListNode(heappop(heap))
            node = node.next
        return head.next

### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            lists: list[list[int]]
            expected: list[int]

        testcases = [
            TestCase(
                name="1",
                lists=[[1,4,5], [1,3,4], [2,6]],
                expected = [1,1,2,3,4,4,5,6]
            ),
        ]

        s = Solution()
        for tc in testcases:
            listNodes = []
            for l in tc.lists:
                listNodes.append(ListNode.toList(l))
            print(listNodes)
            got = s.mergeKLists(listNodes)
            got = ListNode.toArray(got)
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