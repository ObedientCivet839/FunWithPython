### PROBLEM STATEMENT
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

# Given a string s, determine if it is valid.

# A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

# Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
# Return true if s is a valid string, otherwise, return false.

# Example 1:
# Input: s = "aabcbc"
# Output: true
# Explanation:
# "" -> "abc" -> "aabcbc"
# Thus, "aabcbc" is valid.

# Example 2:
# Input: s = "abcabcababcc"
# Output: true
# Explanation:
# "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
# Thus, "abcabcababcc" is valid.

# Example 3:
# Input: s = "abccba"
# Output: false
# Explanation: It is impossible to get "abccba" using the operation.

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        while ("abc" in s):
            s = s.replace("abc", "")
        return not s

    def isValid_1(self, s: str) -> bool:
        if not s:
            return True
        if s.endswith("abc"):
            if self.isValid(s[:-3]):
                return True
        if s.startswith("a") and s.endswith("bc"):
            if self.isValid(s[1:-2]):
                return True
        if s.startswith("ab") and s.endswith("c"):
            if self.isValid(s[2:-1]):
                return True
        if s.startswith("abc"):
            if self.isValid(s[3:]):
                return True
        if s.startswith("a") and s.endswith("c"):
            L = len(s) - 1
            for i in range(1, L):
                if s[i] != "b":
                    continue
                if self.isValid(s[1:i]) and self.isValid(s[i+1:L]):
                    return True
        return False

# "a abc bc a abc bc"
# "a abc b abc c"
# s -> s1 + "abc" or "a" + s2 + "bc" or "ab" + s3 + "c" or "abc" + s4

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