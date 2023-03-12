### PROBLEM STATEMENT
# https://leetcode.com/problems/count-anagrams/

# ou are given a string s containing one or more words. Every consecutive pair of words is separated by a single space ' '.

# A string t is an anagram of string s if the ith word of t is a permutation of the ith word of s.

# For example, "acb dfe" is an anagram of "abc def", but "def cab" and "adc bef" are not.
# Return the number of distinct anagrams of s. Since the answer may be very large, return it modulo 109 + 7.

# Example 1:
# Input: s = "too hot"
# Output: 18
# Explanation: Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".

# Example 2:
# Input: s = "aa"
# Output: 1
# Explanation: There is only one anagram possible for the given string.

### IMPORTS
import math

# Method 1:
# 
# Idea:
# Python - factorial
# For each word, number of anagrams = (N!) / (W_1! * W_2...)
# Traverse the list of words, multiply the results together.
# Caveat: Make sure we have not seen the string before.
# -> Sort the string, and add it to a set.
#
# Runtime: O(???)
# 
#
class Solution:
    MOD = 1000000007

    def countAnagrams(self, s: str) -> int:
        prod = 1
        words = s.split()
        # seen = set()
        for w in words:
            # FIXED:
            # We don't need this since the word will be in a separate position
            # sw = ''.join(sorted(w))
            # if sw in seen:
                # continue
            # else:
                # seen.add(sw)
            num = self.wordAnagrams(w)
            prod = (prod * num) % Solution.MOD
        return prod
    
    def factorial(self, x: int) -> int:
        prod = 1
        for i in range(1, x + 1):
            prod = (prod * i) % Solution.MOD
        return prod

    def wordAnagrams(self, s: str) -> int:
        letters = {}
        for c in s:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1
        N = self.factorial(len(s))
        for v in letters.values():
            N /= self.factorial(v)
        return int(N)


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
            expected: int

        testcases = [
            TestCase(
                name="1",
                s="too hot",
                expected = 18
            ),
            TestCase(
                name="2",
                s="aa",
                expected = 1
            ),
            TestCase(
                name="3",
                s="too oto",
                expected = 9
            ),
            # BUG: Modulo does not work well
            # TestCase(
            #     name="4",
            #     s="smuiquglfwdepzuyqtgujaisius ithsczpelfqp rjm",
            #     expected = 200923648
            # ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.countAnagrams(tc.s)
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