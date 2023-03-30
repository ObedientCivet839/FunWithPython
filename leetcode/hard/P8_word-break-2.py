import functools
### PROBLEM STATEMENT
# https://leetcode.com/problems/word-break-ii/

# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]

# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

# Method 1:
# 
# Idea: Dynamic Programming
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        self.wordDict = wordDict
        b, sentences = self.helper(s, 0)
        res = []
        if b:
            for words in sentences:
                res.append(" ".join(words))
        return res
    
    @functools.cache
    def helper(self, s: str, i: int) -> tuple[bool, list[str]]:
        if i == len(s):
            return (True, [[]])
        if i > len(s):
            return (False, [[]])
        res = []
        for j in range(i+1, len(s)+1):
            ss = s[i:j]
            if ss in self.wordDict:
                found, sres = self.helper(s, j)
                if found:
                    for sentence in sres:
                        res.append([ss] + sentence)
        return (True, res)


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
            wordDict: list[str]
            expected: int

        testcases = [
            TestCase(
                name="1",
                s="catsanddog",
                wordDict=["cat", "cats", "and", "sand", "dog"],
                expected = ["cats and dog", "cat sand dog"]
            ),
            TestCase(
                name="2",
                s = "pineapplepenapple",
                wordDict = ["apple","pen","applepen","pine","pineapple"],
                expected=["pine apple pen apple","pineapple pen apple","pine applepen apple"]
            ),
            TestCase(
                name="3",
                s="catsandog",
                wordDict=["cats", "and", "sand", "dog", "cat"],
                expected = []
            ),
            TestCase(
                name="4",
                s="aaaaaaa",
                wordDict=["aaaa","aa","a"],
                expected = ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.wordBreak(tc.s, tc.wordDict)
            self.assertEqual(
                sorted(tc.expected),
                sorted(got),
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