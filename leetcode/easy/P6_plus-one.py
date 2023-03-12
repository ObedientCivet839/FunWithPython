### PROBLEM STATEMENT
# https://leetcode.com/problems/plus-one/

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        # iterate through the list in reverse
        for i in range(len(digits)-1, -1, -1):
            # new value: need to add the carry
            d = digits[i] + carry
            digits[i] = d % 10
            carry = d // 10
            if carry == 0:
                break
        # extends the list
        if carry > 0:
            digits = [carry] + digits
        return digits

### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            digits: list[int]
            expected: int

        testcases = [
            TestCase(
                name="1",
                digits = [1,2,3],
                expected = [1,2,4],
            ),
            TestCase(
                name="2",
                digits = [4,3,2,1],
                expected = [4,3,2,2],
            ),
            TestCase(
                name="3",
                digits = [9],
                expected = [1,0],
            ),
            TestCase(
                name="4",
                digits = [9]*10,
                expected = [1] + [0]*10,
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.plusOne(tc.digits)
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