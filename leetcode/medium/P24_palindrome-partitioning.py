### PROBLEM STATEMENT
# https://leetcode.com/problems/palindrome-partitioning/

# Given a string s, partition s such that every substring of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = [[str(s[0])]]
        for i in range(1, len(s)):
            c = str(s[i])
            new_results = []
            result_set = set()
            for r in results:
                # Add single character to all partitions
                nr = r + [c]
                key = "_".join(nr)
                if key not in result_set:
                    new_results.append(nr)
                    result_set.add(key)
                for j in range(len(r) - 1, -1, -1):
                    new_string = ''.join(r[j:] + [c])
                    if new_string == new_string[::-1]:
                        nr = r[:j] + [new_string]
                        key = "_".join(nr)
                        if key not in result_set:
                            new_results.append(nr)
                            result_set.add(key)
                        break
            results = new_results
        return results

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
            expected: list[str]

        testcases = [
            TestCase(
                name="1",
                s = "aab",
                expected = [["a","a","b"], ["aa", "b"]]
            ),
            TestCase(
                name="2",
                s = "a",
                expected = [["a"]]
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.partition(tc.s)
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