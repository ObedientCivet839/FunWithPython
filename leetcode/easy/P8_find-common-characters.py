### PROBLEM STATEMENT
# https://leetcode.com/problems/find-common-characters/

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonMap = self.charMap(words[0])
        for word in words:
            wordMap = self.charMap(word)
            newMap = dict()
            for c in commonMap:
                if c in wordMap:
                    newMap[c] = min(commonMap[c], wordMap[c])
            commonMap = newMap
        res = []
        for c in commonMap:
            res.extend([c] * commonMap[c])
        return res

    def charMap(self, word):
        m = dict()
        for c in word:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        return m
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