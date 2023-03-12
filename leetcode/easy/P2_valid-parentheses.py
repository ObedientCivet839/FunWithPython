### PROBLEM STATEMENT

# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        s = [c for c in s]
        stack = []
        while len(s) > 0:
            c = s.pop(0)
            m = {
                "(": ")",
                "[": "]",
                "{": "}"
            }
            if c in m.keys():
                stack.append(c)
            elif c in m.values():
                end = stack.pop()
                if m[end] != c:
                    return False
        if len(stack) > 0:
            return False
        return True

### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_isValid(self):
        @dataclass
        class TestCase:
            name: str
            input: str
            expected: bool

        testcases = [
            TestCase(
                name="1",
                input="()",
                expected=True,
            ),
            TestCase(
                name="2",
                input="()[]{}",
                expected=True,
            ),
            TestCase(
                name="3",
                input="(]",
                expected=False,
            ),
            TestCase(
                name="4",
                input="({[{}]})",
                expected=True,
            ),
            TestCase(
                name="5",
                input="({[{(}]})",
                expected=False,
            ),
            TestCase(
                name="6",
                input="(",
                expected=False,
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.isValid(tc.input)
            self.assertEqual(
                tc.expected, got,
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