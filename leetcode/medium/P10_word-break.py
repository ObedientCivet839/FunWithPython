### PROBLEM STATEMENT
# https://leetcode.com/problems/word-break


# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.N = len(s)
        self.wordSet = set(wordDict)
        # unset: 0
        # true: 1
        # false: 2
        self.M = [0] * (len(s) + 1)
        return self.helper(0)

    def helper(self, i: int) -> bool:
        if i == self.N:
            return True
        if self.M[i] != 0:
            return self.M[i] == 1
        for j in range(i, self.N):
            word = self.s[i:j+1]
            if not word in self.wordSet:
                continue
            if self.helper(j+1):
                self.M[j+1] = 1
                return True
        self.M[i] = 2
        return False

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