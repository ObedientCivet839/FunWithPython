### PROBLEM STATEMENT
# https://leetcode.com/problems/happy-number/

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input: n = 2
# Output: false

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            a = [int(x) for x in str(n)]
            n = sum([x*x for x in a])
            if n in seen:
                return False
        return True

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
            expected: bool

        testcases = [
            TestCase(
                name="1",
                n=19,
                expected = True
            ),
            TestCase(
                name="2",
                n=2,
                expected = False
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.isHappy(tc.n)
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