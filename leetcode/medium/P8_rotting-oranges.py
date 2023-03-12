### PROBLEM STATEMENT
# https://leetcode.com/problems/rotting-oranges/

# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        res = -1 # minutes
        q = [] #FIFO
        R, C = len(grid), len(grid[0])
        numOranges = 0

        # find rotten
        # q functions append, pop(0)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                    numOranges = numOranges + 1
                if grid[r][c] == 1:
                    numOranges = numOranges + 1

        if len(q) == 0 and numOranges > 0:
            return -1

        if len(q) == numOranges:
            return 0
        nextQ = []
        def helper(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return
            # print(grid)
            if  grid[r][c] == 1: # and (r,c) not in visited:
                numOranges -= 1
                grid[r][c] = 2  #visited.add((r-1,c))
                nextQ.append((r,c))

        while q:
            print("Queue:", q)
            r,c = q.pop(0)
            helper(r-1,c)
            helper(r+1,c)
            helper(r,c+1)
            helper(r,c-1)
            if not q:
                print("Next Queue:", nextQ)
                res = res + 1
                print("Minute:", res)
                q = nextQ
                nextQ = []

        # check if any fresh orange remains :D
        if numOranges > 0:
            return -1
        # check if any fresh orange remains :D
        # for r in range(R):
        #     for c in range(C):
        #         if grid[r][c] == 1:
        #             return -1
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
            grid: list[list[int]]
            expected: int

        testcases = [
            TestCase(
                name="1",
                grid = [[2,1,1],[1,1,0],[0,1,1]],
                expected = 4
            ),
            TestCase(
                name="2",
                grid = [[2,1,1],[0,1,1],[1,0,1]],
                expected = -1
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.orangesRotting(tc.grid)
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