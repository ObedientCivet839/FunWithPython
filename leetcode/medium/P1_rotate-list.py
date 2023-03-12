### PROBLEM STATEMENT
# https://leetcode.com/problems/rotate-list/

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Use 2 pointers
# trail_ptr -> 3
# lead_ptr -> 5
# 1 -> 2 -> 3 -> 4 -> 5
# Step 1: 1 -> 2 -> 3 -> 4 -> 5 (-> 1)
# Step 2: 1 -> 2 -> 3 (-> None)  4 -> 5 (-> 1)
# Step 4:  4 -> 5 -> 1 -> 2 -> 3 (-> None)

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toLinkedList(nums: list[int]) -> Optional[ListNode]:
    head = None
    L = len(nums)
    for i in range(L):
        newNode = ListNode(nums[L - 1 - i], head)
        head = newNode
    return newNode

def toArray(linkedlist: Optional[ListNode]) -> list[int]:
    res = []
    ptr = linkedlist
    while ptr != None:
        res.append(ptr.val)
        ptr = ptr.next
    return res

# Method 1:
# 
# Idea:
# 1. Use 2 pointers (start_ptr, end_ptr), separate by k steps
# - Advance the end_ptr to k steps
# - Advance both pointers until end_ptr.next = None
# 2. Set end_ptr.next to head and start_ptr.next = None.
# 
# Runtime: O(N)
# - O(N) to find the length of the list
# - O(N) to advance the pointers
# - O(1) to reroute the nodes
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        trail = head
        lead = head
        for i in range(k):
            # To support k > length:
            # if reach end of list, reset end to head
            if lead == None:
                lead = head
            lead = lead.next
        while lead.next != None:
            # Advance 2 pointers at the same time
            trail = trail.next
            lead = lead.next
        lead.next = head
        res = trail.next
        trail.next = None
        return res

### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test(self):
        @dataclass
        class TestCase:
            name: str
            head: Optional[ListNode]
            k: int
            expected: Optional[ListNode]
        testcases = [
            TestCase(
                name="1",
                head=toLinkedList([1,2,3,4,5]),
                k = 2,
                expected=[4,5,1,2,3],
            ),
            TestCase(
                name="2",
                head=toLinkedList([1,2,3,4,5,6,7,8,9]),
                k = 1,
                expected=[9,1,2,3,4,5,6,7,8],
            ),
            TestCase(
                name="3",
                head=toLinkedList([1,2,3,4,5,6,7,8,9]),
                k = 5,
                expected=[5,6,7,8,9,1,2,3,4],
            ),
            TestCase(
                name="4",
                head=toLinkedList([0,1,2]),
                k = 4,
                expected=[2,0,1],
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.rotateRight(tc.head, tc.k)
            gotList = toArray(got)
            self.assertListEqual(
                tc.expected,
                gotList,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

def main():
    s = Solution()
    print(s)

if __name__ == '__main__':
    # main()
    unittest.main()