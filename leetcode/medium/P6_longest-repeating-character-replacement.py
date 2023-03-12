### PROBLEM STATEMENT
# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        # r = index of the string
        for r in range(len(s)):
            # advance the count of the current letter
            c = s[r]
            count[c] = 1 + count.get(c, 0)
            # max frequency of a letter - current max or the new count of c
            maxf = max(maxf, count[c])

            # l = the start of the window
            # if the count of the rest of the characters is greater than k
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1 # moving l forward (because the window doesn't have enough count)
                l += 1 # increment l

            res = max(res, r - l + 1) # the length of the window (adjust the window)
        return res

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
            k: int
            expected: int

        testcases = [
            TestCase(
                name="1",
                s="ABAB",
                k=2,
                expected = 4
            ),
            TestCase(
                name="2",
                s = "AABABBA",
                k = 1,
                expected = 4
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.characterReplacement(tc.s, tc.k)
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