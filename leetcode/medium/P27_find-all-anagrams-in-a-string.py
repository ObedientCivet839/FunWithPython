### PROBLEM STATEMENT
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "[cba]_eba_[bac]_d", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


# Method 1:
# 
# Idea: Bruceforce 
# - at each index, check if the next substring is anagram
#
# Runtime: O(N^2)
# 
#

# Method 2:
# 
# Idea:
# - Sorted string
#
# Runtime: O(N^2)
# 
#
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        letters = set(p)
        N = len(s)
        PN = len(p)
        # Optimize for letters not in p
        pos = [True] * N
        sorted_p = sorted(p)
        for i in range(N):
            if s[i] not in letters:
                pos[i] = False
                for j in range(PN-1):
                    if 0 <= i+j <= N:
                        pos[i+j] = False
                    if 0 <= i -j <= N:
                        pos[i-j] = False
        res = []
        for i in range(N):
            if not pos(i):
                continue
            substring = sorted(s[i:i+PN])
            if substring == sorted_p:
                res.append(i)
        return res
            

# Method 3:
# 
# Idea:
# - Map with sliding window (using a dictiionary)
#
# Runtime: O(N^2)
# 
#
class Solution2:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        N = len(s)
        PN = len(p)
        if N < PN:
            return []

        keys = {}
        pkeys = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        for l in letters:
            keys[l] = 0
            pkeys[l] = 0
        
        for i in range(PN):
            c = s[i]
            keys[c] += 1

            pc = p[i]
            pkeys[pc] += 1
        
        def str_dict(d):
            res = []
            for k in sorted(d.keys()):
                res.append(str(k) + ":" + str(d[k]))
            return ",".join(res)
        
        res = []
        for i in range(0, N - PN):
            if str_dict(keys) == str_dict(pkeys):
                res.append(i)
            keys[s[i]] -= 1
            keys[s[i+PN]] += 1
        return res
            
# Method 4:
# 
# Idea:
# - Map with sliding window (using an array)
#
# Runtime: O(N^2)
# 
#
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        N = len(s)
        PN = len(p)
        if N < PN:
            return []

        keys = [0] * 26
        pkeys = [0] * 26
        
        def lookup_index(x):
            return ord(x) - ord('a')

        for i in range(PN):
            # set letters of s
            ci = lookup_index(s[i])  # get index of the letter (w.r.t. 'a')
            keys[ci] += 1
            # set letters of p
            pci = lookup_index(p[i])
            pkeys[pci] += 1
        
        res = []
        for i in range(0, N - PN+1):
            if pkeys == keys:
                res.append(i)
            keys[lookup_index(s[i])] -= 1
            if i +PN < N:
                keys[lookup_index(s[i+PN])] += 1
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
            nums: list[int]
            expected: int

        testcases = [
            TestCase(
                name="1",
                nums = ,
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