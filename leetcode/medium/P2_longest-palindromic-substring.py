### PROBLEM STATEMENT
# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest 
# palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Method 1: Bruceforce
# 
# Idea:
# 1. Find all substrings
# 2. Check if the substrings are palindrome
# 3. Return the longest substring
#
# Runtime: O(N^3)
# - N^2 to get all the substrings
# - N to check if the substring is palindrome
#
class Solution_M1:
    def longestPalindrome(self, s: str) -> str:
        maxLen = -1
        maxString = ""
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                ts = s[i:j]
                tl = j - i
                if self.isPalindrome(ts) and tl > maxLen:
                    maxString = ts
                    maxLen = tl
        return maxString

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]


# Method 2: Dynamic Programming
#
# Idea:
# For a string: "babad"

# Memo[N][N]
# findPalindromes(s, i, j)
# findPalindromes(s, i+1, j)
# findPalindromes(s, i, j-1)
# This substring is a palindrome if A[i] == A[j] and isPalindrome[i+1][j-1]
# If i == j or i - j == 1: This is a palindrome
# 
# 1. For each string, we can either use one of
# 2. Check if the substrings are palindrome
# 3. Return the longest substring
#
# Runtime: O(N^3)
# - N^2 to get all the substrings
# - N to check if the substring is palindrome
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        M = []
        for i in range(N):
            M.append([False] * N)
        self.helper(s, 0, N - 1, M)
        print(M)
        # Interpret the result
        maxS = ""
        maxL = -1
        for i in range(N):
            for j in range(N):
                if M[i][j]: # if it's a palindrome
                    tempL = j - i + 1
                    tempS = s[i:j+1]
                    print(tempS)
                    if tempL > maxL:
                        print("picked:", tempS)
                        maxL = tempL
                        maxS = tempS
        return maxS
    
    def helper(self, s: str, i: int, j: int, M: list[list[bool]]):
        """helper finds all the palindromes in the substring s[i:j]
        and store the result in M."""
        # Base case of recursion
        if M[i][j]:
            return
        # Need to set these to True
        if i > j:
            M[i][j] = True
            return
        if i == j:
            print("1:", s[i:j+1])
            M[i][j] = True
            return
        # Remove either end of the string
        self.helper(s, i+1, j, M)
        self.helper(s, i, j-1, M)
        self.helper(s, i+1, j-1, M)
        # Check the case of a palindrome
        if s[i] == s[j] and M[i+1][j-1]:
            print("2:", s[i:j+1])
            M[i][j] = True


### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            input: str
            expected: str

        testcases = [
            TestCase(
                name="1",
                input="babad",
                expected="bab",
            ),
            TestCase(
                name="2",
                input="cbbd",
                expected="bb",
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.longestPalindrome(tc.input)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

def main():
    s = Solution()
    s.longestPalindrome("babad")

if __name__ == '__main__':
    # main()
    unittest.main()