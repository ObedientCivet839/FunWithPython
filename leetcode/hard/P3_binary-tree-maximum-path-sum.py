### PROBLEM STATEMENT
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Definition for a binary tree node.

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

# Method 1:
# 
# Idea:
# - Return a tuple 
# a: maxPathSum that does not end at root
# b: maxPathSum with path MUST end at root
#
# Runtime: O(N) - V is the number of nodes
# 
class Solution_1:
    # Note: Use inner function will slow down execution by a lot
    def helper(self, node: Optional[TreeNode]) -> list[int]:
        """Helper will return 2 values [a,b]
        a: maxPathSum that does not end at root
        b: maxPathSum with path MUST end at root
        """
        if not node:
            # BUG: cannot use math.inf because (math.inf = math.inf + 4)
            return (-100000, -100000)
        left_values = self.helper(node.left)
        right_values = self.helper(node.right)
        
        possible_value_ends_at_root = max(
            left_values[1] + node.val,
            right_values[1] + node.val,
            node.val)
        # print("ends_root:", possible_value_ends_at_root)

        separate_tree_value = left_values[1] + right_values[1] + node.val
        possible_value_not_ends_at_root = max(
            left_values[0],
            # FIXED: Need to take both paths (ends_at_root and not ends_at_root) in left and right subtrees
            left_values[1],
            right_values[0],
            right_values[1],
            separate_tree_value)
        # print("not_ends_root:", possible_value_not_ends_at_root)
        return (possible_value_not_ends_at_root, possible_value_ends_at_root)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        vals = self.helper(root)
        return max(vals)

# https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize result
        self.findMaxUtilRes = float("-inf")
    
        # Compute and return result
        self.findMaxUtil(root)
        return self.findMaxUtilRes

    def findMaxUtil(self, root):
        # Base Case
        if root is None:
            return 0
    
        # l and r store maximum path sum going through left
        # and right child of root respectively
        l = self.findMaxUtil(root.left)
        r = self.findMaxUtil(root.right)
    
        # Max path for parent call of root. This path
        # must include at most one child of root
        max_single = max(max(l, r) + root.val, root.val)
    
        # Max top represents the sum when the node under
        # consideration is the root of the maxSum path and
        # no ancestor of root are there in max sum path
        max_top = max(max_single, l+r + root.val)
    
        # Static variable to store the changes
        # Store the maximum result
        self.findMaxUtilRes = max(self.findMaxUtilRes, max_top)
    
        return max_single
 
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
            expected: int

        testcases = [
            TestCase(
                name="1",
                root=makeTree([1,2,3]),
                expected = 6
            ),
            TestCase(
                name="2",
                root=makeTree([-10,9,20,None,None,15,7]),
                expected = 42
            ),
            TestCase(
                name="3",
                root=makeTree([-10,9,None]),
                expected = 9
            ),
            TestCase(
                name="4",
                root=makeTree([-10]),
                expected = -10
            ),
            TestCase(
                name="5",
                root=makeTree([1,-2,None]),
                expected = 1
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.maxPathSum(tc.root)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

def main():
    # t = makeTree([1,2,3])
    # t = makeTree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    # t = makeTree([1,2,3,4,5,6,7])
    t = makeTree([-10,9,20,None,None,15,7])
    print(t)
    t.printNode()

if __name__ == '__main__':
    # main()
    unittest.main()