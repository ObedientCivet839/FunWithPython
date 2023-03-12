### PROBLEM STATEMENT
# https://leetcode.com/problems/subtree-of-another-tree/

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false


# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printNode(self, level: int = 0):
        print(level * "--", " val:", self.val)
        if self.left:
            print(level * "--", " left:")
            self.left.printNode(level + 1)
        if self.right:
            print(level * "--", " right:")
            self.right.printNode(level + 1)

def makeTree(nums: list[int]) -> Optional[TreeNode]:
    """Note: nums should always be a FULL binary tree"""
    queue = []
    root = TreeNode(nums.pop(0))
    queue.append(root)
    while(len(nums) > 0):
        nextQueue = []
        while(len(queue) > 0):
            node = queue.pop(0)
            ln = nums.pop(0)
            if ln:
                left = TreeNode(ln)
                node.left = left
                nextQueue.append(left)
            rn = nums.pop(0)
            if rn:
                right = TreeNode(rn)
                node.right = right
                nextQueue.append(right)
        queue = nextQueue
    return root


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        if not subRoot:
            return True
        if root.val == subRoot.val:
            if self.isIdenticalTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def isIdenticalTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.isIdenticalTree(a.left, b.left) and self.isIdenticalTree(a.right, b.right)

### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            root: Optional[TreeNode]
            subRoot: Optional[TreeNode]
            expected: bool

        testcases = [
            TestCase(
                name="1",
                root=makeTree([3,4,5,1,2,None,None]),
                subRoot=makeTree([4,1,2]),
                expected = True
            ),
            # TestCase(
            #     name="2",
            #     root=makeTree([3,4,5,1,2,None,None,None,None,0,None,None,None,None,None,None,None,None,None]),
            #     subRoot=makeTree([4,1,2]),
            #     expected = False
            # ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.isSubtree(tc.root, tc.subRoot)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

def main():
    s = Solution()
    # root=makeTree([3,4,5,1,2,None,None])
    root=makeTree([3,4,5,1,2,None,None,None,None,0,None,None,None,None,None,None,None,None,None])
    root.printNode()

if __name__ == '__main__':
    # main()
    unittest.main()