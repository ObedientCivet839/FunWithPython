### PROBLEM STATEMENT
# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Method 1: DFS
# 
# Idea:
# 
#
# Runtime: O((NxM) * 4^(len_of_word))
# 
#
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        # BUG: https://stackoverflow.com/questions/13157961/2d-array-of-zeros
        # This is because (as you read the expression from the inside out), you create a list of C zeros. You then create a list of R references to that initial list of C zeros.
        # visited = [[False] * C] * R
        visited = [[False for i in range(C)] for j in range(R)]

        def printVisited():
            for l in visited:
                print(l)

        def helper(rem: str, r: int, c: int) -> bool:
            if rem == "":
                return True
            # Check out of bounds
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            # False if already visit
            if visited[r][c]:
                return False
            # False if current cell is not the same as remaining word
            if rem[0] != board[r][c]:
                return False

            visited[r][c] = True
            res = helper(rem[1:], r + 1, c) or helper(rem[1:], r - 1, c) or helper(rem[1:], r, c+1) or helper(rem[1:], r, c-1)
            visited[r][c] = False
            return res

        for r in range(R):
            for c in range(C):
                visited = [[False for i in range(C)] for j in range(R)]
                if helper(word, r, c):
                    return True
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
            board: list[list[str]]
            word: str
            expected: bool

        testcases = [
            TestCase(
                name="1",
                board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
                word = "ABCCED",
                expected=True
            ),
            TestCase(
                name="2",
                board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
                word = "SEE",
                expected=True
            ),
            TestCase(
                name="3",
                board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
                word = "ABCB",
                expected=False
            ),
            TestCase(
                name="4",
                board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
                word = "ABCESEEEFS",
                expected=True
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.exist(tc.board, tc.word)
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