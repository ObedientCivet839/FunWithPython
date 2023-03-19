### PROBLEM STATEMENT
# https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# Method 1:
# 
# Idea: Encode each character based on the order of appearance
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        es = self.encode(s)
        et = self.encode(t)
        return es == et
    
    def encode(self, s: str) -> str:
        count = 0
        cm = dict() # map from character to number
        res = ""
        for c in s:
            if c not in cm:
                cm[c] = count
                count += 1
            res += str(cm[c]) + "_" # output format: ex. 0_1_3_12
        return res

# Method 2:
# 
# Idea:
# - Keep a map of character from S to T.
# - Make sure that there cannot be 2 characters in S that map to the same character in T.
#
# Runtime: O(???)
# 
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cm = dict()
        for i in range(len(s)):
            if s[i] not in cm:
                # if we already have a mapping to T[i] previously
                if t[i] in cm.values():
                    return False
                cm[s[i]] = t[i]
            else:
                if cm[s[i]] != t[i]:
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
            s: str
            t: str
            expected: bool

        testcases = [
            TestCase(
                name="1",
                s="egg",
                t="add",
                expected = True
            ),
            TestCase(
                name="2",
                s="foo",
                t="bar",
                expected = False
            ),
            TestCase(
                name="3",
                s="paper",
                t="title",
                expected = True
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.isIsomorphic(tc.s, tc.t)
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