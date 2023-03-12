### PROBLEM STATEMENT
# https://leetcode.com/problems/set-matrix-zeroes/

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# Notes: Can also use an Array or mark the start of the rows, cols
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = matrix
        zeroRows, zeroCols = set(), set()
        R = len(M)
        C = len(M[0])
        for r in range(R):
            for c in range(C):
                if M[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)
        
        for r in zeroRows:
            for c in range(C):
                M[r][c] = 0

        for c in zeroCols:
            for r in range(R):
                M[r][c] = 0


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