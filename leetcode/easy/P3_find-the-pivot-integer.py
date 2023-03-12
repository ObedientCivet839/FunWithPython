### PROBLEM STATEMENT
# https://leetcode.com/problems/find-the-pivot-integer/

# Given a positive integer n, find the pivot integer x such that:

# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

# Example 1:
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 is the pivot integer since: 1 = 1.

# Example 3:
# Input: n = 4
# Output: -1
# Explanation: It can be proved that no such integer exist.


# Method 1:
# 
# Idea:
# - Traverse the array from 2 sides
# - If left_sum < right_sum -> left_ptr++, else right_ptr--
# - Until left_ptr == right_ptr
#
# Runtime: O(???)
# 
#
class Solution_M1:
    def pivotInteger(self, n: int) -> int:
        leftPtr, rightPtr = 1, n
        leftSum, rightSum = 1, n
        while leftPtr < rightPtr:
            # print("ptr:", leftPtr, rightPtr)
            # print("sum:", leftSum, rightSum)
            if leftSum <= rightSum:
                leftPtr += 1
                leftSum += leftPtr
            else:
                rightPtr -= 1
                rightSum += rightPtr
        if leftPtr == rightPtr and leftSum == rightSum:
            return leftPtr
        return -1

# Method 2: Mathematic formulas
# 
# Idea:
# Sum of consecutive integers
#   (# of items) / 2 * (sum of first and last elem)
# 
# x .... n -> (n - x + 1) * (n + x) / 2
#
# => x = sqrt((n^2 + n) / 2)
#
# Runtime: O(1)
# 
class Solution:
    def pivotInteger(self, n: int) -> int:
        import math
        x = math.sqrt((n*n + n) / 2)
        # Check that the value of x is a whole number
        if x == int(x):
            return int(x)
        return -1
  

### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            n: int
            expected: int

        testcases = [
            TestCase(
                name="1",
                n=8,
                expected = 6
            ),
            TestCase(
                name="2",
                n=1,
                expected = 1
            ),
            TestCase(
                name="3",
                n=4,
                expected=-1
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.pivotInteger(tc.n)
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
    # main()
    unittest.main()